package main

import (
	"fmt"
	"time"
)

func main() {
	msg := make(chan string)
	go greet(msg)
	time.Sleep(2 * time.Second)

	greeting := <-msg

	time.Sleep(2 * time.Second)
	fmt.Println("Greeting received")
	fmt.Println(greeting)
}

func greet(ch chan string) {
	fmt.Println("Greeter waiting to send greeting!")

	ch <- "Hello Rwitesh"

	fmt.Println("Greeter completed")
}