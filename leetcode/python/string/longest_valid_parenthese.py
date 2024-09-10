# https://leetcode.com/problems/longest-valid-parentheses
"""
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses
substring
Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
"""
from collections import deque


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        dp = []  # result of the string that ends at i
        ans = 0
        for t in range(len(s)):
            if t == 0:
                dp.append(0)
                continue
            if s[t] == '(':
                dp.append(0)
                continue
            stack = deque()
            stack.append(s[t])
            x = t  # x is the first index such that s[x:t+1] is valid
            while x >= 1 and stack:
                x -= 1
                top = stack[-1]
                if top == ')' and s[x] == '(':
                    stack.pop()
                else:
                    stack.append(s[x])

            if stack:  # that means x = 0
                dp.append(0)
                continue
            if x == 0:
                dp.append(t+1)
            else:
                res = dp[x-1] + t - x + 1
                dp.append(res)
            ans = max(ans, dp[-1])
        return ans


s = "))))((()(("
sol = Solution()
ans = sol.longestValidParentheses(s)
print(ans)
