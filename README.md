# Algorithm
```
g++ -std=c++17 practice/cpp/template.cpp && ./a.out
```

# Python

# Golang
- Khi cap = 1, thì buffered channel chứa được một giá trị và không block main goroutine. Trong khi đó unbuffered channel sẽ block ngay.
```
package main

func main() {
	bufferedChan := make(chan int, 1)
	unbufferedChan := make(chan int)

	bufferedChan <- 1   // OK
	unbufferedChan <- 1 // deadlock
}
```
- [Concurrent Programming in Go – Goroutines, Channels, and More Explained with Examples](https://www.freecodecamp.org/news/concurrent-programming-in-go/)