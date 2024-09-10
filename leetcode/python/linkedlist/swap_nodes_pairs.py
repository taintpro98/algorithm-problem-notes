# https://leetcode.com/problems/swap-nodes-in-pairs/
"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.) 
Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""
from typing import Optional
from utils import ListNode, array_to_linked_list, linked_list_to_array


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while head and head.next:
            first_node = head
            second_node = head.next
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            prev = first_node
            head = first_node.next
        return dummy.next


head = array_to_linked_list([1, 2, 3, 4])
sol = Solution()
ans = sol.swapPairs(head)
print(linked_list_to_array(ans))
