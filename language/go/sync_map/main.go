package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	var m sync.Map
	var wg sync.WaitGroup

	for i := 0; i < 10; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			time.Sleep(time.Duration(i) * time.Second)
			m.Store(fmt.Sprintf("key%d", i), fmt.Sprintf("value%d", i))
		}(i)
	}

	wg.Wait()

	m.Range(func(key, value interface{}) bool {
		fmt.Println("Key:", key, "Value:", value)
		return true
	})
}
