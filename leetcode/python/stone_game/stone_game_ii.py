# https://leetcode.com/problems/stone-game-ii/
"""
Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i]. The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. Then, we set M = max(M, X). Initially, M = 1.

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.
Example 1:

Input: piles = [2,7,9,4,4]

Output: 10

Explanation:

If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 stones in total.
If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 stones in total.
So we return 10 since it's larger.

Example 2:

Input: piles = [1,2,3,4,5,100]

Output: 104
Constraints:

1 <= piles.length <= 100
1 <= piles[i] <= 104
"""

"""
dp[i][j] - start at i, with M = m
dp[0][1] = ?
1 <= X <= 2*j
p[i] = sum from i
dp[i][j] = max(
	Sum - dp[x+i][max(x,j)]
)
1 <= x <= min(2j, n-i)

i = x
j = max(x, j)

case i = j = 1
when x == 1
dp[1][1] = S - min(dp[x][max(x, j)])
"""

from typing import List
class Solution:
    def handle(self, dp: List[List[int]], piles: List[int], prs: List[int], i: int, j: int) -> int:
        if i >= len(piles):
            dp[i][j] = 0
            return 0
        if i == len(piles) - 1:
            dp[i][j] = piles[-1]
            return piles[-1]
        if dp[i][j] != -1:
            return dp[i][j]
        n = len(piles)
        upper = min(j + j, n-i)
        bob = self.handle(dp, piles, prs, i+1, max(1, j))
        for x in range(2, upper + 1):
            bob = min(bob, self.handle(dp, piles, prs, x + i, max(x, j)))
        dp[i][j] = prs[n] - prs[i] - bob
        return dp[i][j]

    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[-1] * 300 for _ in range(n+1)]
        prs = [0]
        for t in piles:
            prs.append(t+prs[-1])
        self.handle(dp, piles, prs, 0, 1)
        return dp[0][1]


piles = [66,100,40,49,4,39,82,47,86,79,84,33,5,14,97,2,95,75,24,20]
sol = Solution()
ans = sol.stoneGameII(piles)
print(ans)
