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
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        visited = set()
        queue = deque([(startGene, 0)])
        while queue:
            node = queue.popleft()
            print(node)
            if node[0] == endGene:
                return node[1]
            if node[0] not in visited:
                visited.add(node[0])
                for idx, (s, e) in enumerate(zip(node[0], endGene)):
    	            if s != e:
                        tmp = node[0][:idx] + e + node[0][idx + 1:]
                        print("idx", idx)
                        print("tmp", tmp)
                        if tmp in bank_set:
                            queue.append((tmp, node[1] + 1))
        return -1
        
    
startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]
sol = Solution()
ans = sol.minMutation(startGene, endGene, bank)
print(ans)