# https://leetcode.com/problems/stone-game
"""
Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.

Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.

Example 1:

Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alice starts first, and can only take the first 5 or the last 5.
Say she takes the first 5, so that the row becomes [3, 4, 5].
If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alice, so we return true.
Example 2:

Input: piles = [3,7,2,3]
Output: true

Constraints:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles[i]) is odd.
"""

"""
dp[i][i] = invalid <= because the number has to be odd
dp[i][i+1] = piles[i]
dp[i][j] = max()
- = sum[i][j] - |dp[i][j-1]|
"""
from typing import List

class Solution:
    def handle(self, dp: List[List[int]], piles: List[int], pr: List[int], i: int, j: int) -> int:
        if dp[i][j] != -1:
            return dp[i][j]
        if i == j:
            dp[i][i] = 0
            return 0
        if j - i == 1:
            dp[i][j] = piles[i]
            return dp[i][j]
        sumPiles = pr[j] - pr[i]
        if self.handle(dp, piles, pr, i, j-1) > 0: # if Bob wins i, j-1
            a = sumPiles - self.handle(dp, piles, pr, i, j-1) # the number of piles Alice has
            if a >= self.handle(dp, piles, pr, i, j-1):
                dp[i][j] = a
            else:
                dp[i][j] = -self.handle(dp, piles, pr, i, j-1)
        else: # if Alice wins i, j-1
            dp[i][j] = piles[j-1] + abs(self.handle(dp, piles, pr, i, j-1)) # Alice wins i, j
            
        if self.handle(dp, piles, pr, i+1, j) > 0: #if Bob wins i+1, j
            a = sumPiles - self.handle(dp, piles, pr, i+1, j) # the number of piles Alice has
            if a >= self.handle(dp, piles, pr, i+1, j):
                dp[i][j] = max(dp[i][j], a)
            else:
                dp[i][j] = max(dp[i][j], -self.handle(dp, piles, pr, i+1, j))
        else: # Alice wins i+1, j
            dp[i][j] = max(dp[i][j], piles[i] + abs(self.handle(dp, piles, pr, i+1, j)))
        return dp[i][j]
            
        
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        pr = [0]
        for i in range(n):
            pr.append(piles[i] + pr[-1])
        dp = [[-1] * (n+1) for _ in range(n)]
        self.handle(dp, piles, pr, 0, n)
        return self.handle(dp, piles, pr, 0, n) > 0
        
piles = [3,7,2,3]
sol = Solution()
ans = sol.stoneGame(piles)
print(ans)
