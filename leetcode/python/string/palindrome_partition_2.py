# https://leetcode.com/problems/palindrome-partitioning-ii/
"""
Given a string s, partition s such that every 
substring of the partition is a palindrome

Return the minimum cuts needed for a palindrome partitioning of s.
Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1

Constraints:

1 <= s.length <= 2000
s consists of lowercase English letters only.
"""
from typing import List


class Solution:
    def minCut(self, s: str) -> List[List[str]]:
        dp = [[-1] * len(s) for _ in range(len(s))]
        for b in range(len(s)):
            for a in range(b + 1):
                if a == b:
                    dp[a][b] = 1
                elif s[a] != s[b]:
                    dp[a][b] = 0
                else:  # s[a] = s[b]
                    if a == b-1:
                        dp[a][b] = 1
                    else:
                        dp[a][b] = dp[a+1][b-1]
        ndp = [-1]  # ans of the string with the length t
        for t in range(1, len(s) + 1):
            if t == 1:
                ndp.append(0)
                continue
            minv = -2
            for x in range(t):
                if dp[x][t-1] == 1:
                    if minv == -2:
                        minv = ndp[x]
                    else:
                        minv = min(minv, ndp[x])
            ndp.append(1+minv)
        return ndp[len(s)]


s = "efe"
sol = Solution()
ans = sol.minCut(s)
print(ans)
