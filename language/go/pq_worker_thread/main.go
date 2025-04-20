package main

import (
	"fmt"
	"sync"
	"time"
	"container/heap"
)

// Task represents a job with priority
type Task struct {
	ID       int
	Priority int // Higher value means higher priority
}

// PriorityQueue implements a max-heap for tasks
type PriorityQueue []*Task

func (pq PriorityQueue) Len() int { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].Priority > pq[j].Priority // Max-heap: higher priority first
}
func (pq PriorityQueue) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }
func (pq *PriorityQueue) Push(x interface{}) {
	*pq = append(*pq, x.(*Task))
}
func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	*pq = old[0 : n-1]
	return item
}

// WorkerPool manages the dynamic pool of workers
type WorkerPool struct {
	tasks       chan *Task      // Channel for task submission
	pq          PriorityQueue   // Priority queue for tasks
	maxWorkers  int             // Maximum number of workers
	currentWorkers int          // Current number of active workers
	wg          sync.WaitGroup  // WaitGroup to track worker completion
	mu          sync.Mutex      // Mutex to protect shared state
	stop        chan struct{}   // Signal to stop the pool
}

// NewWorkerPool initializes a new WorkerPool
func NewWorkerPool(maxWorkers int, bufferSize int) *WorkerPool {
	pool := &WorkerPool{
		tasks:      make(chan *Task, bufferSize),
		pq:         make(PriorityQueue, 0),
		maxWorkers: maxWorkers,
		stop:       make(chan struct{}),
	}
	heap.Init(&pool.pq)
	return pool
}

// worker processes tasks with a timeout
func (wp *WorkerPool) worker(id int) {
	defer func() {
		wp.mu.Lock()
		wp.currentWorkers--
		wp.mu.Unlock()
		wp.wg.Done()
	}()

	for {
		select {
		case task := <-wp.tasks:
			fmt.Printf("Worker %d started task %d (priority %d)\n", id, task.ID, task.Priority)
			time.Sleep(1 * time.Second) // Simulate work
			fmt.Printf("Worker %d finished task %d\n", id, task.ID)
		case <-time.After(2 * time.Second): // Idle timeout
			wp.mu.Lock()
			if wp.currentWorkers > 1 && wp.pq.Len() == 0 { // Keep at least 1 worker
				fmt.Printf("Worker %d timed out and exited, total workers: %d\n", id, wp.currentWorkers-1)
				wp.mu.Unlock()
				return
			}
			wp.mu.Unlock()
		case <-wp.stop:
			return
		}
	}
}

// AddTask submits a task and dynamically adjusts workers
func (wp *WorkerPool) AddTask(task *Task) {
	wp.mu.Lock()
	heap.Push(&wp.pq, task)
	wp.tasks <- task
	queueSize := wp.pq.Len()
	if wp.currentWorkers < queueSize && wp.currentWorkers < wp.maxWorkers {
		wp.currentWorkers++
		wp.wg.Add(1)
		go wp.worker(wp.currentWorkers)
		fmt.Printf("Spawned new worker, total workers: %d\n", wp.currentWorkers)
	}
	wp.mu.Unlock()
}

// Run starts the pool with an initial worker
func (wp *WorkerPool) Run() {
	wp.mu.Lock()
	if wp.currentWorkers == 0 {
		wp.currentWorkers++
		wp.wg.Add(1)
		go wp.worker(wp.currentWorkers)
		fmt.Println("Started initial worker")
	}
	wp.mu.Unlock()
}

// Shutdown gracefully stops the pool
func (wp *WorkerPool) Shutdown() {
	wp.mu.Lock()
	close(wp.tasks) // Stop accepting new tasks
	close(wp.stop)  // Signal workers to stop
	wp.mu.Unlock()
	wp.wg.Wait()    // Wait for all workers to finish
	fmt.Println("Pool shut down gracefully!")
}

func main() {
	// Create a worker pool with a maximum of 3 workers
	pool := NewWorkerPool(3, 10)

	// Start the pool
	pool.Run()

	// Submit tasks with different priorities
	tasks := []Task{
		{ID: 1, Priority: 1},
		{ID: 2, Priority: 3},
		{ID: 3, Priority: 2},
		{ID: 4, Priority: 5},
		{ID: 5, Priority: 1},
	}
	for i := range tasks {
		pool.AddTask(&tasks[i])
		time.Sleep(200 * time.Millisecond) // Small delay to observe behavior
	}

	// Wait a bit to see timeout in action, then shutdown
	time.Sleep(5 * time.Second)
	pool.Shutdown()
}