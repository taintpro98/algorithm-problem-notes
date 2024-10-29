# https://leetcode.com/problems/count-primes
"""
Given an integer n, return the number of prime numbers that are strictly less than n.
Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0

Constraints:

0 <= n <= 5 * 106
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        primes = n * [1]
        r = n // 2 + 1
        for t in range(2, r):
            m = t + t
            while m < n:
                primes[m] = 0
                m += t
        ans = sum(primes)
        return ans - 2
    
n = 5
sol = Solution()
ans = sol.countPrimes(n)
print(ans)