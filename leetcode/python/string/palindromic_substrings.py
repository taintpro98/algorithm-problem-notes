# https://leetcode.com/problems/palindromic-substrings
"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]
        ans = 0
        for b in range(n):
            for a in range(b+1):
                if a == b:
                    dp[a][b] = 1
                elif s[a] != s[b]:
                    dp[a][b] = 0
                else: # s[a] = s[b]
                    if a + 1 == b:
                        dp[a][b] = 1
                    else:
                        dp[a][b] = dp[a+1][b-1]
                ans += dp[a][b]
        return ans


s = "aaa"
sol = Solution()
ans = sol.countSubstrings(s)
print(ans)
