# https://leetcode.com/problems/longest-happy-string
"""
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.
Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.

Constraints:

0 <= a, b, c <= 100
a + b + c > 0

"""
"""
Ta sẽ giải bài này bằng thuật toán tham lam. 
Đầu tiên sử dụng một max heap để lưu tần suất còn lại của các ký tự. 
Mỗi lần ta sẽ chọn ra phần tử xuất hiện nhiều nhất và thỏa mãn điều kiện để thêm vào substring đáp án. 
Cho tới khi nào không thể chọn được nữa thì thôi. 
Sau mỗi lần như vậy ta phải cập nhật lại maxheap. 

We will solve this problem using a greedy algorithm. First, we use a max heap to store the remaining frequency of characters.
Each time, we will select the most frequent character that satisfies the condition to be added to the resulting substring.
We continue this process until no more characters can be selected.
After each selection, we need to update the max heap.
"""
import heapq
class Solution:
    def isValid(self, ans: str, e: str) -> bool:
        if len(ans) < 2:
            return True
        if ans[-1] != ans[-2]:
            return True
        if e != ans[-1]:
            return True
        return False
    
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heapq.heappush(heap, [-a, "a"])
        if b > 0:
            heapq.heappush(heap, [-b, "b"])
        if c > 0:
            heapq.heappush(heap, [-c, "c"])
        ans = ""
        while heap:
            tmp = []
            count = len(heap)
            runOfOut = False
            for i in range(count):
                node = heapq.heappop(heap)
                if self.isValid(ans, node[1]):
                    ans += node[1]
                    node[0] = node[0] + 1
                    tmp.append(node)
                    break
                else:
                    tmp.append(node)
                    if i == count - 1:
                        runOfOut = True
                        break
            if runOfOut:
                break
            for item in tmp:
                if item[0] < 0:
                    heapq.heappush(heap, item)
        return ans
    
a = 7
b = 1
c = 0
sol = Solution()
ans = sol.longestDiverseString(a, b, c)
print(ans)