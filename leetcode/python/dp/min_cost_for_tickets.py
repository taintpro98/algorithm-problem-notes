# https://leetcode.com/problems/minimum-cost-for-tickets
"""
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.
Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total, you spent $17 and covered all the days of your travel.

Constraints:

1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000
"""
from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        days = [0] + days
        min_cost = costs[0]
        min_day = 1
        for idx, c in zip([1,7,30], costs):
            if c < min_cost:
                min_cost = c
                min_day = idx
        dp = [0, min_cost] + (n-1) * [-1] # minimum solutions that ends at i (non-decreasing array)
        s = [0, days[0] + min_day - 1] + (n-1) * [-1] # non-decreasing array
        for i in range(2, n + 1):
            if s[i-1] >= days[i]:
                dp[i] = dp[i-1]
                s[i] = s[i-1]
            else:
                dp[i] = dp[i-1] + min_cost
                s[i] = days[i]
                for j in range(i-1, 0, -1):
                    if days[i] - days[j] <= 6:
                        tmp = dp[j - 1] + costs[1]
                        if tmp < dp[i]:
                            dp[i] = tmp
                            s[i] = days[j] + 6
                    elif days[i] - days[j] <= 29:
                        tmp = dp[j-1] + costs[2]
                        if tmp < dp[i]:
                            dp[i] = tmp
                            s[i] = days[j] + 29
        return dp[-1]
    
days = [1,7]
costs = [3,2,1]
sol = Solution()
ans = sol.mincostTickets(days, costs)
print(ans)