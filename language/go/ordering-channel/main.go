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

func (data []Item) []int{
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
	close(resultCh)

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
	ans := 
}
