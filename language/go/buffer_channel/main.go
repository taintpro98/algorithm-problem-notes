package main

import (
	"errors"
	"fmt"
	"sync"
	"time"
)

type Item struct {
	ID int
}

func handle(data Item) error {
	time.Sleep(time.Duration(10-data.ID) * time.Second)
	if data.ID%2 == 0 {
		return nil
	}
	return errors.New("error")
}

func execute1(data []Item) []int {
	var wg sync.WaitGroup
	wg.Add(len(data))
	resultCh := make(chan int, len(data))
	for _, item := range data {
		go func(
			wg *sync.WaitGroup,
			vs Item,
			dataChannel chan<- int,
		) {
			defer wg.Done()
			err := handle(vs)
			if err == nil {
				dataChannel <- vs.ID
			}
		}(&wg, item, resultCh)
	}
	wg.Wait()
	// close(resultCh)
	fmt.Println("wait")

	var response []int
	for result := range resultCh {
		fmt.Println(result)
		response = append(response, result)
	}
	close(resultCh)
	fmt.Println("for")
	return response
}

func execute2(data []Item) []int {
	var wg sync.WaitGroup
	wg.Add(len(data))
	resultCh := make(chan int, len(data))
	for _, item := range data {
		go func(
			wg *sync.WaitGroup,
			vs Item,
			dataChannel chan<- int,
		) {
			defer wg.Done()
			err := handle(vs)
			if err == nil {
				dataChannel <- vs.ID
			}
		}(&wg, item, resultCh)
	}
	go func() {
		wg.Wait()
		close(resultCh) // we have to close the channel in this go routine so that the main routine can stop listen for new data 
	}()

	var response []int
	for result := range resultCh {
		response = append(response, result)
	}
	return response
}

func main() {
	data := []Item{{
		ID: 1,
	}, {
		ID: 2,
	}, {
		ID: 3,
	}, {
		ID: 4,
	}, {
		ID: 5,
	}, {
		ID: 6,
	}}
	ans := execute1(data)
	fmt.Println(ans)
}
