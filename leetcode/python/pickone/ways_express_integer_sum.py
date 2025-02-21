# https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers
"""
Given two positive integers n and x.

Return the number of ways n can be expressed as the sum of the xth power of unique positive integers, in other words, the number of sets of unique integers [n1, n2, ..., nk] where n = n1x + n2x + ... + nkx.

Since the result can be very large, return it modulo 109 + 7.

For example, if n = 160 and x = 3, one way to express n is n = 23 + 33 + 53.

Example 1:

Input: n = 10, x = 2
Output: 1
Explanation: We can express n as the following: n = 32 + 12 = 10.
It can be shown that it is the only way to express 10 as the sum of the 2nd power of unique integers.
Example 2:

Input: n = 4, x = 1
Output: 2
Explanation: We can express n in the following ways:
- n = 41 = 4.
- n = 31 + 11 = 4.

Constraints:

1 <= n <= 300
1 <= x <= 5
"""
class Solution:
    def __init__(self):
        self.power = [0]
        
    def multiply(self, n: int, x: int) -> None:
        for i in range(1, n+1):
            k = 1
            for _ in range(x):
                k *= i
            if k <= n:
                self.power.append(k)
            else:
                break
            
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        self.multiply(n, x)
        k = len(self.power) - 1
        dp = [[0] * (k + 1) for _ in range (n+1)] # dp[i][j] means the result of the sum i with the max element j
        for i in range(n + 1):
            for j in range(1, k+1):
                if i == 1:
                    dp[i][j] = 1
                    continue
                dp[i][j] = dp[i][j-1]
                if self.power[j] == i:
                    dp[i][j] += 1
                elif self.power[j] < i:
                    dp[i][j] += dp[i-self.power[j]][j-1]
                dp[i][j] %= MOD
        return dp[n][k]
        
        
n = 10
x = 2
sol = Solution()
ans = sol.numberOfWays(n, x)
print(ans)
"""
dp[10][2] = 1
dp[0][1] = 0
dp[0][2] = 0
dp[4][4] = 1 + dp[4][3]
dp[4][3] = dp[4][2] + dp[1][2]
dp[1][2] = dp[1][1] = 1
"""

# 1DP array solution 
"""
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        power = []
        
        # Precompute powers
        i = 1
        while i**x <= n:
            power.append(i**x)
            i += 1

        dp = [0] * (n + 1)
        dp[0] = 1  # There's one way to sum up to 0 (using nothing)
        
        # Fill DP table
        for p in power:
            for i in range(n, p - 1, -1):  # Traverse in reverse to avoid reusing elements
                dp[i] = (dp[i] + dp[i - p]) % MOD
        return dp[n]
"""