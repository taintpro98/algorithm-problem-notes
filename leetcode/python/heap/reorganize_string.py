# https://leetcode.com/problems/reorganize-string
"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.
Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
"""
from collections import defaultdict
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        heap = [(-v, k) for k, v in count.items()]
        heapq.heapify(heap)
        ans = ""
        num_chars = len(s)
        while heap:
            tmp = []
            for _ in range(2):
                if heap:
                    node = heapq.heappop(heap)
                    tmp.append((node[0] + 1, node[1]))
                
                if len(ans) > 0 and node[1] == ans[-1]:
                    return ""
                num_chars -= 1
                ans += node[1]
                if num_chars <= 0:
                    break
            for item in tmp:
                if item[0] < 0:
                    heapq.heappush(heap, item)
        return ans
    
s = "aaab"
sol = Solution()
ans = sol.reorganizeString(s)
print(ans)