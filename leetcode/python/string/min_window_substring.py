# https://leetcode.com/problems/minimum-window-substring
"""
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chardict = defaultdict(int)
        charset = set()
        for c in t:
            chardict[c] = chardict[c] + 1
            charset.add(c)
        l = 0
        ans = ""
        count = 0  # the number characters satisfied
        charcount = defaultdict(int)
        for r in range(len(s)):
            if s[r] in charset:
                if charcount[s[r]] == chardict[s[r]] - 1:
                    count += 1
                charcount[s[r]] += 1
            
            while l < r and (s[l] not in charset or charcount[s[l]] > chardict[s[l]]):
                charcount[s[l]] -= 1
                l += 1
            if count >= len(charset):
                if ans == "" or len(ans) > r-l+1:
                    ans = s[l:r+1]
        return ans


s = "acbbaca"
t = "aba"
sol = Solution()
ans = sol.minWindow(s, t)
print(ans)
