# https://leetcode.com/problems/word-search/

from typing import List


class Solution:
    def __init__(self) -> None:
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def backtrack(
        self,
        board: List[List[str]],
        visited,
        word,
        curIdx,
        idx,
        jdx,
        ans
    ):
        if curIdx >= len(word):
            return
        if word[curIdx] != board[idx][jdx]:
            return
        if curIdx == len(word) - 1:
            ans[0] = True
            return
        for (x, y) in self.directions:
            ni, nj = x + idx, y + jdx
            if ni < len(board) and ni >= 0 and nj >=0 and nj < len(board[0]) and (ni, nj) not in visited:
                visited.add((ni, nj))
                self.backtrack(board, visited, word, curIdx+1, ni, nj, ans)
                visited.remove((ni, nj))

    def exist(self, board: List[List[str]], word: str) -> bool:
        result = [False]
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                visited.add((i, j))
                self.backtrack(board, visited, word, 0, i, j, result)
                if result[0]:
                    return True
        return result[0]


if __name__ == "__main__":
    sol = Solution()

    board = [
        ["A", "B", "C", "E"], 
        ["S", "F", "C", "S"], 
        ["A", "D", "E", "E"]
    ]
    word = "ABCCED"
    result = sol.exist(board, word)
    print(result)
