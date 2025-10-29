# https://leetcode.com/problems/burst-balloons
"""
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.
Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
Example 2:

Input: nums = [1,5]
Output: 10

Constraints:

n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100
"""
from typing import List


class Solution:
	def maxCoins(self, nums: List[int]) -> int:
		A = [1] + nums + [1]
		n = len(A)
		dp = [n * [0] for _ in range(n)]
		for length in range(n-1):
			for l in range(n-length-1):
				r = length + l + 1
				for k in range(l+1, r):
					dp[l][r] = max(dp[l][r], A[k] * A[l] * A[r] + dp[l][k] + dp[k][r])
		return dp[0][n-1]


nums = [3, 1, 5, 8]
sol = Solution()
ans = sol.maxCoins(nums)
print(ans)
