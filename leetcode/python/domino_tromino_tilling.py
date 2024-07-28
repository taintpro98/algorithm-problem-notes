# https://leetcode.com/problems/domino-and-tromino-tiling

class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
        MOD = 10**9 + 7
        sum = (n+1) * [0]
        dp = (n + 1) * [-1]
        dp[1], dp[2], dp[3] = 1, 2, 5
        sum[1], sum[2], sum[3] = 2, 4, 9
        for i in range(4, n+1):
            dp[i] = (dp[i-1] + dp[i-2]) % MOD
            dp[i] = (dp[i] + 2 * sum[i-3]) % MOD
            sum[i] = (sum[i-1] + dp[i]) % MOD
        return dp[n]

n = 4
sol = Solution()
ans = sol.numTilings(n)
print(ans)