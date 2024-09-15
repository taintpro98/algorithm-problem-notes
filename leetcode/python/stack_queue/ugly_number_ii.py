# https://leetcode.com/problems/ugly-number-ii
"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return the nth ugly number.
Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
 
Constraints:

1 <= n <= 1690
"""
import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        visited = set([1])
        ugly = []
        heapq.heappush(ugly, 1)
        t = 1
        for _ in range(1, n+1):
            t = heapq.heappop(ugly)
            i2 = t * 2
            i3 = t * 3
            i5 = t * 5
            if i2 not in visited:
                visited.add(i2)
                heapq.heappush(ugly, i2)
            if i3 not in visited:
                visited.add(i3)
                heapq.heappush(ugly, i3)
            if i5 not in visited:
                visited.add(i5)
                heapq.heappush(ugly, i5)
        return t


n = 10
sol = Solution()
ans = sol.nthUglyNumber(n)
print(ans)
