# https://leetcode.com/problems/basic-calculator
"""
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
"""


class Solution:
    def calPostFix(self, s: str) -> int:
        stack = []
        a = s.strip().split(' ')
        print(s)
        print(a)
        for c in a:
            if c.isdigit():
                stack.append(c)
            else:
                if not stack:
                    return None
                b = int(stack.pop())
                if not stack:
                    return None
                a = int(stack.pop())
                if c == '+':
                    stack.append(a + b)
                elif c == '-':
                    stack.append(a - b)
        return int(stack[-1])

    def calculate(self, s: str) -> int:
        postfix = ""
        stack = []
        num = ''
        for c in s:
            if c == ' ':
                continue
            if c.isdigit():
                num += c
            else:
                if num != '':
                    postfix += ' ' + num
                    num = ''
                if c == '(':
                    stack.append(c)
                if c == ')':
                    while stack and stack[-1] != '(':
                        postfix += ' ' + stack.pop()
                    stack.pop()
                elif c == '+' or c == '-':
                    while stack and stack[-1] == '-':
                        postfix += ' ' + stack.pop()
                    stack.append(c)
        if num != '':
            postfix += ' ' + num
            num = ''
        while stack:
            postfix += ' ' + stack.pop()
        return self.calPostFix(postfix)


s = "1-(     -2)"
sol = Solution()
ans = sol.calculate(s)
print(ans)
