# https://leetcode.com/problems/sliding-window-maximum
"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
"""
from typing import List
import heapq
from utils import MaxHeap
from collections import defaultdict


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        ans = []
        tmp = nums[0]
        max_heap = MaxHeap()
        mydict = defaultdict(int)
        for i in range(k):
            tmp = max(tmp, nums[i])
            max_heap.push(nums[i])
            mydict[nums[i]] += 1
        ans.append(tmp)

        for i in range(1, len(nums) - k + 1):
            prev_max = ans[-1]
            mydict[nums[i-1]] -= 1

            if nums[i-1] == prev_max:
                while mydict[prev_max] == 0 and max_heap.size() > 1:
                    max_heap.pop()
                    prev_max = max_heap.top()
            if nums[i+k-1] > prev_max:
                ans.append(nums[i+k-1])
            else:
                ans.append(prev_max)
                
            max_heap.push(nums[i+k-1])
            mydict[nums[i+k-1]] += 1
        return ans


k = 5
nums = [9, 10, 9, -7, -4, -8, 2, -6]
sol = Solution()
ans = sol.maxSlidingWindow(nums, k)
print(ans)
