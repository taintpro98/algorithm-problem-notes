# https://leetcode.com/problems/redundant-connection
"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

Example 1:

Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:

Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""
from typing import List
from collections import defaultdict

class Solution:
    def dfs(self, graph: defaultdict, visited: set, cycle: List[int], parent: int, node: int) -> bool:
        visited.add(node)
        cycle.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if self.dfs(graph, visited, cycle, node, neighbor):
                    return True
            elif neighbor != parent:
                cycle.append(neighbor)
                return True
        cycle.pop()
        return False
    
    def isValid(self, u: int, v: int, cycleSet: set) -> bool:
        return str(u) + "_" + str(v) in cycleSet or str(v) + "_" + str(u) in cycleSet
    
    def normalize(self, cycle: List[int]) -> List[int]:
        i = 0
        while cycle[i] != cycle[-1]:
            i += 1
        return cycle[i:]
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        n = 1
        for u, v in edges:
            n = max(n, u, v)
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        cycle = []
        for i in range(1, n+1):
            if i not in visited:
                if self.dfs(graph, visited, cycle, -1, i):
                    break
        cycle = self.normalize(cycle)
        cycleSet = set()
        for i in range(len(cycle) - 1):
            cycleSet.add(str(cycle[i]) + "_" +  str(cycle[i+1]))
        cycleSet.add(str(cycle[0]) + "_" + str(cycle[len(cycle)-1]))
        for i in range(len(edges) - 1, -1, -1):
            u, v = edges[i]
            if self.isValid(u, v, cycleSet):
                return edges[i]
        return []
    
edges = [[20,24],[3,17],[17,20],[8,15],[14,17],[6,17],[15,23],[6,8],[15,19],[16,22],[7,9],[8,22],[2,4],[4,11],[22,25],[6,24],[13,19],[15,18],[1,9],[4,9],[4,19],[5,10],[4,21],[4,12],[5,6]]
sol = Solution()
ans = sol.findRedundantConnection(edges)
print(ans)