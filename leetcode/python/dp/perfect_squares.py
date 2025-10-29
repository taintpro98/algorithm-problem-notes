# https://leetcode.com/problems/perfect-squares
"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Constraints:

1 <= n <= 104
"""
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n+1) # results at n = i
        dp[1] = 1
        squares = []
        t,x = 1,1
        while x <= n:
            squares.append(x)
            t += 1
            x = t*t
        for i in range(2, n+1):
            for j in squares:
                if j > i:
                    break
                if dp[i] == 0:
                    dp[i] = 1 + dp[i-j]
                else:
                    dp[i] = min(dp[i], 1+dp[i-j])
        return dp[-1]
    
n = 13
sol = Solution()
ans = sol.numSquares(n)
print(ans)