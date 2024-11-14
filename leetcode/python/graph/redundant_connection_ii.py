# https://leetcode.com/problems/redundant-connection-ii
"""
In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with n nodes (with distinct values from 1 to n), with one additional directed edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [ui, vi] that represents a directed edge connecting nodes ui and vi, where ui is a parent of child vi.

Return an edge that can be removed so that the resulting graph is a rooted tree of n nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:

Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:

Input: edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
Output: [4,1]

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ui, vi <= n
ui != vi
"""
# a rooted tree is a directed graph
from typing import List
from collections import defaultdict

class Solution:
    # def DFS(self, graph: defaultdict, rec_stack: set, visited: set, cycle: List[int], node: int) -> bool:
    #     visited.add(node)
    #     rec_stack.add(node)
    #     cycle.append(node)
        
    #     for neighbor in graph[node]:
    #         if neighbor not in visited:
    #             if self.DFS(graph, rec_stack, visited, cycle, neighbor):
    #                 return True
    #         elif neighbor in rec_stack:
    #             cycle.append(neighbor)
    #             return True
        
    #     rec_stack.remove(node)
    #     cycle.pop()
    #     return False
    
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
    
    def normalize(self, cycle: List[int]) -> List[int]:
        i = 0
        while cycle[i] != cycle[-1]:
            i += 1
        return cycle[i:]
    
    def isValid(self, u: int, v: int, cycleSet: set, inDegree: List[int], maxInDegree: int) -> bool:
        return (str(u) + "_" + str(v) in cycleSet or str(v) + "_" + str(u) in cycleSet) and inDegree[v] == maxInDegree
    
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        n = 1
        for u, v in edges:
            n = max(n, u, v)
            graph[u].append(v)
            graph[v].append(u)
        in_degree = [0] * (n + 1)
        for u, v in edges:
            in_degree[v] += 1
            
        visited = set()
        cycle = []
        for i in range(1, n+1):
            if i not in visited:
                if self.dfs(graph, visited, cycle, -1, i):
                    break
        
        cycle = self.normalize(cycle)
        print(cycle)
        maxInDegree = 0
        for c in cycle:
            maxInDegree = max(maxInDegree, in_degree[c])
        cycleSet = set()
        for i in range(len(cycle) - 1):
            cycleSet.add(str(cycle[i]) + "_" +  str(cycle[i+1]))
        cycleSet.add(str(cycle[0]) + "_" + str(cycle[len(cycle)-1]))
        for i in range(len(edges) - 1, -1, -1):
            u, v = edges[i]
            if self.isValid(u, v, cycleSet, in_degree, maxInDegree):
                return edges[i]
        return []
        
# edges = [[4,2],[1,5],[5,2],[5,3],[2,4]]
edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
sol = Solution()
ans = sol.findRedundantDirectedConnection(edges)
print(ans)