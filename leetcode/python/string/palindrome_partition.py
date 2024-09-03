# https://leetcode.com/problems/palindrome-partitioning/
"""
Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.
Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 
Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
"""
from typing import List

class Solution:
    def backtrack(
            self,
            s: str,
            ans: List[List[str]],
            tmp: List[str],
            curlen: int
        ):
        if curlen == len(s):
            ans.append(tmp.copy())
            return
        for t in range(curlen, len(s)):
            if self.dp[curlen][t] == 1:
                tmp.append(s[curlen:t+1])
                newlen = t + 1
                self.backtrack(s, ans, tmp, newlen)
                tmp.pop()
    
    def partition(self, s: str) -> List[List[str]]:
        self.dp = [[-1] * len(s) for _ in range(len(s))]
        for b in range(len(s)):
            for a in range(b + 1):
                if a == b:
                    self.dp[a][b] = 1
                elif s[a] != s[b]:
                    self.dp[a][b] = 0
                else: # s[a] = s[b]
                    if a == b-1:
                        self.dp[a][b] = 1
                    else:
                        self.dp[a][b] = self.dp[a+1][b-1]
        res = []
        tmp = []
        self.backtrack(s, res, tmp, 0)
        return res

s = "a"
sol = Solution()
ans = sol.partition(s)
print(ans)