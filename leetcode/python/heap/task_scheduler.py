# https://leetcode.com/problems/task-scheduler
"""
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.
Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:

Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.
Constraints:

1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100
"""
from typing import List
from collections import defaultdict
# import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = defaultdict(int)
        for t in tasks:
            count[t] += 1
        # heap = []
        # for c in count:
        #     heapq.heappush(heap, (-count[c], c))
        rows = []
        while len(count) > 0:
            rows.append(len(count))
            for c in count:
                count[c] -= 1
            zero_keys = [k for k, v in count.items() if v == 0]
            for z in zero_keys:
                del count[z]
        ans = len(tasks)
        for t in range(len(rows) - 1):
            if rows[t]-1 < n:
                ans += (n-rows[t]+1)
        return ans
    
tasks = ["B","C","D","A","A","A","A","G"]
n = 1
sol = Solution()
ans = sol.leastInterval(tasks, n)
print(ans)
"""
ABCDG
A
A
A
"""