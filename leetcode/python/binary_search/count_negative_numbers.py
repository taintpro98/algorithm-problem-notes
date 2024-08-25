# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix
"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
 

Follow up: Could you find an O(n + m) solution?
"""
from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        l, r = 0, n-1
        count = 0
        for i in range(m):
            l = 0
            while l < r:
                mid = l + (r-l)//2
                if grid[i][mid] < 0:
                    r = mid
                else:
                    l = mid + 1
            if grid[i][r] < 0:
                count += (n - r)
        return count
    
grid = [[3,2],[1,0]]
sol = Solution()
ans = sol.countNegatives(grid)
print(ans)