# https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}
        ans = 0
        l, r = 0, 0
        for r in range(len(s)):
            c = s[r]
            if c in char_dict:
                last = char_dict[c]
                while l <= last:
                    del char_dict[s[l]]
                    l += 1
            ans = max(ans, r-l+1)
            char_dict[c] = r
        return ans


s = "pwwkew"
sol = Solution()
ans = sol.lengthOfLongestSubstring(s)
print(ans)
