# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # the max element that equals the target
        l, r = 0, len(nums)-1
        rp = -1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                l = mid + 1
                rp = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if rp == -1:
            return [-1, -1]
        l, r = 0, rp
        lp = rp
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                r = mid - 1
                lp = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return [lp, rp]


nums = [5,7,7,8,8,10]
target = 6
sol = Solution()
ans = sol.searchRange(nums, target)
print(ans)
