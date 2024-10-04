# https://leetcode.com/problems/create-maximum-number
"""
You are given two integer arrays nums1 and nums2 of lengths m and n respectively. nums1 and nums2 represent the digits of two numbers. You are also given an integer k.

Create the maximum number of length k <= m + n from digits of the two numbers. The relative order of the digits from the same array must be preserved.

Return an array of the k digits representing the answer.
Example 1:

Input: nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
Output: [9,8,6,5,3]
Example 2:

Input: nums1 = [6,7], nums2 = [6,0,4], k = 5
Output: [6,7,6,0,4]
Example 3:

Input: nums1 = [3,9], nums2 = [8,9], k = 3
Output: [9,8,9]

Constraints:

m == nums1.length
n == nums2.length
1 <= m, n <= 500
0 <= nums1[i], nums2[i] <= 9
1 <= k <= m + n
"""
from typing import List
class Solution:
    def maxSingleArray(self, nums: List[int], k) -> List[int]:
        drop = len(nums) - k
        stack = []
        for num in nums:
            while drop and stack and stack[-1] < num:
                stack.pop()
                drop -= 1
            stack.append(num)
        return stack[:k]
    
    def merge(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        i = j = 0
        while i < len(nums1) or j < len(nums2):
            if i >= len(nums1):
                ans.append(nums2[j])
                j += 1
            elif j >= len(nums2):
                ans.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1
        return ans
        
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        ans = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            curr = self.merge(
                self.maxSingleArray(nums1, i),
                self.maxSingleArray(nums2, k-i)
            )
            ans = max(ans, curr)
        return ans
    
nums1 = [6,7]
nums2 = [6,0,4]
k = 5
sol = Solution()
ans = sol.maxNumber(nums1, nums2, k)
print(ans)