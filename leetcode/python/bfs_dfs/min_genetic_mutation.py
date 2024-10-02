# https://leetcode.com/problems/minimum-genetic-mutation
"""
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2

Constraints:

0 <= bank.length <= 10
startGene.length == endGene.length == bank[i].length == 8
startGene, endGene, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
"""
from typing import List
from collections import deque, defaultdict

class Solution:
    def isAdj(self, gen1: str, gen2: str) -> bool:
        if len(gen1) != len(gen2):
            return False
        count = 0
        for a, b in zip(gen1, gen2):
            if a != b:
                count += 1
            if count > 1:
                return False
        return count == 1
    
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        graph = defaultdict(list)
        for b in bank:
            if self.isAdj(startGene, b):
                graph[startGene].append(b)
                graph[b].append(startGene)
        for i in range(len(bank) - 1):
            for j in range(i+1, len(bank)):
                if self.isAdj(bank[j], bank[i]):
                    graph[bank[i]].append(bank[j])
                    graph[bank[j]].append(bank[i])

        visited = set()
        queue = deque([(startGene, 0)])
        visited.add(startGene)

        while queue:
            node = queue.popleft()
            if node[0] == endGene:
                return node[1]
            for next in graph[node[0]]:
                if next not in visited:
                    visited.add(next)
                    queue.append((next, node[1] + 1))
        return -1
    
startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]
sol = Solution()
ans = sol.minMutation(startGene, endGene, bank)
print(ans)

"""
AACCGGTT -> 
AACCGATT
AACCGATA
AAACGATA
AAACGGTA
"""