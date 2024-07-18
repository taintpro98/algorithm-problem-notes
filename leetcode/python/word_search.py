# https://leetcode.com/problems/word-search/

from typing import List


class Solution:
    def backtrack(
        self,
        board: List[List[str]],
        word,
        curIdx
    ):
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.backtrack()

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.backtrack(board, word, )
