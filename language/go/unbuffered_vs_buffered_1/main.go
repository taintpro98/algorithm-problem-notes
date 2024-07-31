package main

import "fmt"

func worker(t <-chan int){
	fmt.Println(<- t)
}

func main() {
	// bufferedChan := make(chan int, 1)
	unbufferedChan := make(chan int)

	// bufferedChan <- 1   // OK
	// unbufferedChan <- 1 // deadlock
	// go worker(unbufferedChan)
	<-unbufferedChan
}