# https://leetcode.com/problems/make-sum-divisible-by-p
"""
Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.

Example 1:

Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.
Example 2:

Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.
Example 3:

Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= p <= 109
"""
from typing import List
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        r = sum(nums) % p
        if r == 0:
            return 0
        prefix = {}
        curr = 0
        ans = len(nums)
        for idx, n in enumerate(nums):
            curr = (curr + n) % p
            prefix_sum = (curr - r) % p
            if prefix_sum in prefix:
                ans = min(ans, idx - prefix[prefix_sum])
            elif prefix_sum == 0:
                ans = min(ans, idx + 1)
            prefix[curr] = idx
        return ans if ans < len(nums) else -1
    
nums = [8,32,31,18,34,20,21,13,1,27,23,22,11,15,30,4,2]
p = 148
sol = Solution()
ans = sol.minSubarray(nums, p)
print(ans)
"""
prefix[j] - prefix[i] mod p = r => prefix[j] - r mod p = prefix[i]
"""