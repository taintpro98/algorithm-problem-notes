# https://leetcode.com/problems/non-overlapping-intervals/description/?envType=study-plan-v2&envId=leetcode-75
"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104
"""
from typing import List


def isOverlap(inter1: List[int], inter2: List[int]) -> bool:
    start1, end1 = inter1
    start2, end2 = inter2
    return start1 < end2 and start2 < end1


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        end = intervals[0][1]
        count = 0
        for idx in range(1, len(intervals)):
            if intervals[idx][0] >= end:
                end = intervals[idx][1]
            else:
                count += 1
        return count


intervals = [[1, 2], [1, 2], [1, 2]]
sol = Solution()
ans = sol.eraseOverlapIntervals(intervals)
print(ans)
