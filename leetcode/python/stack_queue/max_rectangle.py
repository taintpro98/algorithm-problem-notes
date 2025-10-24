# https://leetcode.com/problems/maximal-rectangle
"""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1

Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
"""
from typing import List

class Solution:
	def largestRectangleArea(self, heights: List[int]) -> int:
		stack = []
		ans = 0
		for (idx, h) in enumerate(heights + [0]):
			while stack and heights[stack[-1]] >= h:
				top = stack[-1]
				stack.pop()
				l = -1
				if stack:
					l = stack[-1]
				ans = max(ans, heights[top] * (idx - l - 1))
			stack.append(idx)
		return ans

	def maximalRectangle(self, matrix: List[List[str]]) -> int:
		R, C = len(matrix), len(matrix[0])
		ans = 0
		for r in range(R):
			h = []
			for c in range(C):
				if matrix[r][c] == "0":
					h.append(0)
				else:
					t = r
					hs = 0
					while t < R and matrix[t][c] == "1":
						hs += 1
						t += 1
					h.append(hs)
			ans = max(ans, self.largestRectangleArea(h))
		return ans

matrix = [["1"]]
sol = Solution()
ans = sol.maximalRectangle(matrix)
print(ans)
