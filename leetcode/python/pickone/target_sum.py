# https://leetcode.com/problems/target-sum
"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
"""
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        maxsum = sum(nums)
        if maxsum < abs(target):
            return 0
        dp = [[0] * (maxsum + 1) for _ in range (n+1)] # dp[i][j] = result with i elements and target = j
        for i in range(n+1):
            for j in range(maxsum + 1):
                if i == 0:
                    if j != 0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = 1 
                    continue
                if i == 1:
                    if nums[i-1] == abs(j):
                        if nums[i-1] == 0:
                            dp[i][j] = 2
                        else:
                            dp[i][j] = 1
                    else:
                        dp[i][j] = 0
                    continue
                dp[i][j] = dp[i-1][abs(j - nums[i-1])]
                if j + nums[i-1] <= maxsum:
                    dp[i][j] += dp[i-1][j + nums[i-1]]
        return dp[n][abs(target)]
    
nums = [1,1,1,1,1]
target = 3
sol = Solution()
ans = sol.findTargetSumWays(nums, target)
print(ans)
"""
dp[0][x] = 0 with x != 0
dp[i][j] = dp[i-1][abs(j - nums[i-1])] + dp[i-1][abs(j + nums[i-1])] 
"""