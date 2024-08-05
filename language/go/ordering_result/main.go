package main

import (
	"fmt"
	"sync"
)

// Kết quả của mỗi công việc, bao gồm cả lỗi nếu có
type Result struct {
	Index int         // Vị trí của phần tử trong mảng ban đầu
	Value interface{} // Giá trị xử lý
	Error error       // Lỗi nếu có
}

func main() {
	data := []int{1, 2, 3, 4, 5} // Mảng ban đầu
	var wg sync.WaitGroup        // WaitGroup để đợi các goroutine hoàn thành
	resultCh := make(chan Result, len(data))

	for i, v := range data {
		wg.Add(1)
		go func(index int, value int) {
			defer wg.Done()
			result, err := process(value)
			resultCh <- Result{Index: index, Value: result, Error: err}
		}(i, v)
	}

	go func() {
		wg.Wait()
		close(resultCh)
	}()

	results := make([]interface{}, len(data)) // Mảng kết quả
	for result := range resultCh {
		if result.Error != nil {
			fmt.Printf("Error processing index %d: %v\n", result.Index, result.Error)
			continue
		}
		results[result.Index] = result.Value
	}

	// Lọc kết quả để loại bỏ các phần tử bị lỗi
	finalResults := make([]interface{}, 0, len(results))
	for _, res := range results {
		if res != nil {
			finalResults = append(finalResults, res)
		}
	}

	fmt.Println("Processed results:", finalResults)
}

func process(value int) (interface{}, error) {
	if value%2 == 0 { // Giả sử các giá trị chẵn sẽ gặp lỗi
		return nil, fmt.Errorf("processing error for value %d", value)
	}
	return value * 2, nil // Xử lý giá trị (ở đây là nhân đôi)
}
