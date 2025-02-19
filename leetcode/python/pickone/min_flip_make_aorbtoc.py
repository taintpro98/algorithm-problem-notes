#https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/description/?envType=study-plan-v2&envId=leetcode-75
"""
Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.
Example 1:

Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
Example 2:

Input: a = 4, b = 2, c = 7
Output: 1
Example 3:

Input: a = 1, b = 2, c = 3
Output: 0
 

Constraints:

1 <= a <= 10^9
1 <= b <= 10^9
1 <= c <= 10^9
"""
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        abin = bin(a)[2:]
        bbin = bin(b)[2:]
        cbin = bin(c)[2:]
        maxlength = max(len(abin), len(bbin), len(cbin))
        abin = abin.zfill(maxlength)
        bbin = bbin.zfill(maxlength)
        cbin = cbin.zfill(maxlength)
        count = 0
        for t in range(maxlength):
            if cbin[t] == '0':
                count += (abin[t] == '1') + (bbin[t] == '1')
            else:
                if abin[t] == '0' and bbin[t] == '0':
                    count += 1
        return count
    
a = 2
b = 6
c = 5
sol = Solution()
ans = sol.minFlips(a, b, c)
print(ans)