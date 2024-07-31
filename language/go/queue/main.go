package main

import (
	"fmt"
	"sync"
	"time"
)

type Task struct {
	ID      int
	Message string
}

func worker(id int, tasks <-chan Task, wg *sync.WaitGroup) {
	defer wg.Done()
	for task := range tasks {
		fmt.Printf("Worker %d processing task: %d - %s\n", id, task.ID, task.Message)
		time.Sleep(time.Second) // Giả lập việc xử lý công việc
	}
}

func main() {
	numTasks := 50
	numWorkers := 3
	tasks := make(chan Task, numTasks)
	var wg sync.WaitGroup
	for idx := 0; idx < numWorkers; idx++ {
		wg.Add(1)
		go worker(idx, tasks, &wg)
	}

	for i := 0; i < numTasks * 2; i++ {
		tasks <- Task{ID: i, Message: fmt.Sprintf("Task %d processed", i)}
	}
	
	close(tasks)
	wg.Wait()
	fmt.Println("All tasks completed.")
}
