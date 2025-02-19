# https://leetcode.com/problems/n-queens
"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]

Constraints:

1 <= n <= 9
"""
from typing import List


class Solution:
    def create(self, t: int, n: int) -> str:
        ans = ''
        for i in range(n):
            if i == t:
                ans += 'Q'
            else:
                ans += '.'
        return ans

    def backtrack(self, n: int, ans: List[List[str]], tmp: List[str], vds: List[List[bool]], vcs: List[bool], curRow: int) -> None:
        if len(tmp) == n:
            ans.append(tmp.copy())
            return
        for i in range(n):
            ld = curRow + i
            rd = curRow + n - i - 1
            if not vcs[i] and not vds[0][ld] and not vds[1][rd]:
                row = self.create(i, n)
                tmp.append(row)
                vcs[i] = True
                vds[0][ld] = True
                vds[1][rd] = True
                self.backtrack(n, ans, tmp, vds, vcs, curRow+1)
                vcs[i] = False
                vds[0][ld] = False
                vds[1][rd] = False
                tmp.pop()

    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        tmp = []
        vds = [[False] * (2*n - 1) for _ in range(2)]
        vcs = n * [False]
        self.backtrack(n, res, tmp, vds, vcs, 0)
        return res


n = 4
sol = Solution()
ans = sol.solveNQueens(n)
print(ans)
