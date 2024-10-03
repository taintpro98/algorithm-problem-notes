# https://leetcode.com/problems/triangle
"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10

Constraints:

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104
"""
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1] * n for _ in range(n)] # dp[i][j] represents rows i, col j
        for i in range (n):
            if i == 0:
                dp[0][0] = triangle[0][0]
            else:
                for j in range(i+1):
                    if j == 0:
                        dp[i][j] = dp[i-1][j] + triangle[i][j]
                    elif j == i:
                        dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        ans = float('inf')
        for t in range(n):
            if dp[n-1][t] < ans:
                ans = dp[n-1][t]
        return ans
                
            

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]] 
sol = Solution()
ans = sol.minimumTotal(triangle)
print(ans)