package main

import (
	"fmt"
	"sync"
	"time"
)

// Task represents a job to be processed
type Task struct {
	ID int
}

// WorkerPool manages the dynamic pool of workers
type WorkerPool struct {
	tasks       chan Task       // Task queue
	maxWorkers  int             // Maximum number of workers allowed
	currentWorkers int          // Current number of active workers
	wg          sync.WaitGroup  // WaitGroup to track worker completion
	mu          sync.Mutex      // Mutex to protect shared state
}

// NewWorkerPool initializes a new WorkerPool
func NewWorkerPool(maxWorkers int, bufferSize int) *WorkerPool {
	return &WorkerPool{
		tasks:      make(chan Task, bufferSize),
		maxWorkers: maxWorkers,
	}
}

// worker processes tasks and exits when no tasks remain
func (wp *WorkerPool) worker(id int) {
	defer func() {
		wp.mu.Lock()
		wp.currentWorkers--
		wp.mu.Unlock()
		wp.wg.Done()
	}()

	for task := range wp.tasks {
		fmt.Printf("Worker %d started task %d\n", id, task.ID)
		time.Sleep(1 * time.Second) // Simulate work
		fmt.Printf("Worker %d finished task %d\n", id, task.ID)
	}
}

// AddTask submits a task and dynamically adjusts workers
func (wp *WorkerPool) AddTask(task Task) {
	wp.tasks <- task

	wp.mu.Lock()
	defer wp.mu.Unlock()

	// If there are fewer workers than tasks in queue and below maxWorkers, spawn a new worker
	if wp.currentWorkers < len(wp.tasks) && wp.currentWorkers < wp.maxWorkers {
		wp.currentWorkers++
		wp.wg.Add(1)
		go wp.worker(wp.currentWorkers)
		fmt.Printf("Spawned new worker, total workers: %d\n", wp.currentWorkers)
	}
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

// Wait waits for all workers to finish
func (wp *WorkerPool) Wait() {
	close(wp.tasks) // Close the channel to signal workers to stop
	wp.wg.Wait()    // Wait for all workers to complete
}

func main() {
	// Create a worker pool with a maximum of 3 workers and a task buffer of 10
	pool := NewWorkerPool(3, 10)

	// Start the pool with one initial worker
	pool.Run()

	// Submit 5 tasks
	for i := 1; i <= 5; i++ {
		pool.AddTask(Task{ID: i})
		time.Sleep(200 * time.Millisecond) // Small delay to observe worker spawning
	}

	// Wait for all tasks to complete
	pool.Wait()
	fmt.Println("All tasks completed!")
}