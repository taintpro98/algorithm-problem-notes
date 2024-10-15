# https://leetcode.com/problems/maximum-sum-circular-subarray
"""
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
 
Constraints:

n == nums.length
1 <= n <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
"""
from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # firstly, I find the maximum non-empty subarray
        total = sum(nums)
        cur = 0
        ans = total
        for i in range(len(nums)):
            if i == 0:
                cur = nums[i]
            elif cur > 0:
                cur += nums[i]
            else:
                cur = nums[i]
            ans = max(cur, ans)
        # secondly, need to find minimum subarray
        min_ans = 0
        leng = 0
        for i in range(len(nums)):
            if i == 0:
                cur = nums[i]
                leng = 1
            elif cur < 0:
                cur += nums[i]
                leng += 1
            else:
                cur = nums[i]
                leng = 1
            if leng != len(nums):
                min_ans = min(min_ans, cur)
        ans = max(ans, total - min_ans)
        return ans

nums = [-3,-2,-3]
sol = Solution()
ans = sol.maxSubarraySumCircular(nums)
print(ans)