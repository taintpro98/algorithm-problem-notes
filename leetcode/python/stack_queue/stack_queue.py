# https://leetcode.com/problems/implement-stack-using-queues
#
# use 2 queues to implement a stack
from collections import deque


class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        res = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return res

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        res = self.q1.popleft()
        self.q2.append(res)
        self.q1, self.q2 = self.q2, self.q1
        return res

    def empty(self) -> bool:
        return len(self.q1) == 0


class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        while len(self.s1) > 1:
            self.s2.append(self.s1.pop())
        res = self.s1.pop()
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())
        return res

    def peek(self) -> int:
        while len(self.s1) > 1:
            self.s2.append(self.s1.pop())
        res = self.s1[-1]
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())
        return res

    def empty(self) -> bool:
        return len(self.s1) == 0
