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
- [Go sync.Cond, the Most Overlooked Sync Mechanism](https://victoriametrics.com/blog/go-sync-cond)
- [Go Concurrency, Why Not?](https://medium.com/@stev3npy/go-concurrency-why-not-1b3b60a47634)
- [Learning Go in 2024; From Beginner to Senior](https://www.bytesizego.com/blog/learning-golang-2024)

# English

### 🧩 **1. Xác nhận hiểu đề**

1. **"Let me make sure I understand the problem correctly."**
2. **"So, we are given \[...], and we need to return \[...], right?"**

---

### 🔍 **2. Làm rõ yêu cầu, hỏi constraints**

3. **"What are the constraints on the input size?"**
4. **"Can the input contain duplicates or negative numbers?"**
5. **"Is the input guaranteed to be sorted?"**

---

### 🧠 **3. Trình bày hướng giải & lựa chọn cấu trúc**

6. **"I’ll first try a brute-force approach to understand the problem."**
7. **"I think we can optimize it using a hashmap to reduce the time complexity."**
8. **"This problem reminds me of \[...], I think a similar technique applies here."**
9. **"We can use a two-pointer approach since the array is sorted."**

---

### 🏗️ **4. Giải thích cách cài đặt**

10. **"I’ll start by initializing \[...]."**
11. **"Then I’ll iterate through the array and do \[...]."**
12. **"At each step, I will check if \[...]."**
13. **"If the condition is met, I will return \[...]."**
14. **"Otherwise, I’ll continue the loop."**

---

### 📈 **5. Phân tích độ phức tạp**

15. **"The time complexity is O(n) because we loop through the array once."**
16. **"The space complexity is O(n) due to the extra storage used by the hashmap."**

---

### 🚧 **6. Xử lý edge case**

17. **"Let’s think about the edge cases."**
18. **"If the input is empty or has only one element, we should return null."**
19. **"Another edge case is when \[...], which we should handle explicitly."**

---

### 🎯 **7. Tổng kết & chốt lại**

20. **"To summarize, I’m using \[...], and this solution handles all edge cases with optimal time and space complexity."**