# https://leetcode.com/problems/longest-increasing-path-in-a-matrix
"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
"""
from typing import List

class Solution:
    def inbound(self, x: int, size: int) -> bool:
        return x >= 0 and x < size
        
    def dfs(self, matrix: List[List[int]], cache: List[List[int]], x: int, y: int) -> int:
        if cache[x][y] != 0:
            return cache[x][y]
        for pathX, pathY in self.paths:
            newX = x + pathX
            newY = y + pathY
            if self.inbound(newX, len(matrix)) and self.inbound(newY, len(matrix[0])) and matrix[x][y] < matrix[newX][newY]:
                cache[x][y] = max(cache[x][y], self.dfs(matrix, cache, newX, newY))
        cache[x][y] += 1
        return cache[x][y]
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        self.paths = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ans = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, self.dfs(matrix, cache, i, j))
        return ans
    
matrix = [[1]]
sol = Solution()
ans = sol.longestIncreasingPath(matrix)
print(ans)