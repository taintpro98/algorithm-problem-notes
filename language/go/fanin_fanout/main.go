package main

import (
	"context"
	"sync"
)

// Fan-Out function
func fanOut[T any](
	ctx context.Context,
	input <-chan T,
	numWorkers int,
	processor func(T) T,
) []<-chan T {
	outputs := make([]<-chan T, numWorkers)

	for i := 0; i < numWorkers; i++ {
		outputs[i] = worker(ctx, input, processor)
	}

	return outputs
}

// Worker function
func worker[T any](
	ctx context.Context,
	input <-chan T,
	processor func(T) T,
) <-chan T {
	output := make(chan T)

	go func() {
		defer close(output)
		for {
			select {
			case <-ctx.Done():
				return
			case val, ok := <-input:
				if !ok {
					return
				}
				select {
				case output <- processor(val):
				case <-ctx.Done():
					return
				}
			}
		}
	}()

	return output
}

// Fan-In function
func fanIn[T any](
	ctx context.Context,
	channels ...<-chan T,
) <-chan T {
	merged := make(chan T)
	var wg sync.WaitGroup

	// Merge function for each channel
	merge := func(ch <-chan T) {
		defer wg.Done()
		for {
			select {
			case <-ctx.Done():
				return
			case val, ok := <-ch:
				if !ok {
					return
				}
				select {
				case merged <- val:
				case <-ctx.Done():
					return
				}
			}
		}
	}

	wg.Add(len(channels))
	for _, ch := range channels {
		go merge(ch)
	}

	// Close merged channel after all inputs are done
	go func() {
		wg.Wait()
		close(merged)
	}()

	return merged
}

func main() {

}
