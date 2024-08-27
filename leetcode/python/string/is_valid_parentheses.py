
# is valid parentheses
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        char_dict = {
            '(': -1,
            ')': 1,
            '[': -2,
            ']': 2,
            '{': -3,
            '}': 3
		}
        for c in s:
            if stack:
                if char_dict[c] < 0:
                    stack.append(c)
                else:
                    top = stack[-1]
                    if char_dict[top] + char_dict[c] != 0:
                        return False
                    stack.pop()
            else:
                stack.append(c)
        return not stack

s = "(){}}{"
sol = Solution()
ans = sol.isValid(s)
print(ans)