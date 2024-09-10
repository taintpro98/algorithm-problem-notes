import heapq


class MaxHeap:
    def __init__(self) -> None:
        self.heap = []

    def size(self) -> int:
        return len(self.heap)

    def push(self, x: int) -> None:
        heapq.heappush(self.heap, -x)

    def pop(self) -> int:
        return -heapq.heappop(self.heap)

    def top(self) -> int:
        return -self.heap[0] if self.heap else None


class GeneralHeap:
    def __init__(self, key=lambda x: x):
        self.heap = []
        self.key = key  # Hàm lambda được truyền vào để xác định tiêu chí so sánh

    def push(self, item):
        # Lưu trữ tuple với tiêu chí so sánh là `self.key(item)` và phần tử `item`
        heapq.heappush(self.heap, (self.key(item), item))

    def pop(self):
        return heapq.heappop(self.heap)[1]

    def peek(self):
        return self.heap[0][1] if self.heap else None

    def size(self):
        return len(self.heap)
