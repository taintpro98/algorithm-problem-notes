# https://leetcode.com/problems/edit-distance
"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
"""


class Solution:
    def handle(self, word1: str, word2: str, a: int, b: int):
        if a == 0:
            self.dp[a][b] = b
            return b
        if b == 0:
            self.dp[a][b] = a
            return a
        if self.dp[a][b] != -1:
            return self.dp[a][b]
        if word1[a-1] == word2[b-1]:
            self.dp[a][b] = self.handle(word1, word2, a-1, b-1)
            return self.dp[a][b]
        self.dp[a][b] = min(self.handle(word1, word2, a-1, b), self.handle(word1, word2, a, b-1), self.handle(word1, word2, a-1, b-1)) + 1
        return self.dp[a][b]
    def minDistance(self, word1: str, word2: str) -> int:
        self.dp = [[-1 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)] # answer with a characters of word1 and b characters of word2
        return self.handle(word1, word2, len(word1), len(word2))

sol = Solution()
word1, word2 = 'horse', 'ros'
ans = sol.minDistance(word1, word2)
print(ans)