from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        # Ghi đè phương thức __lt__ để so sánh các ListNode dựa trên giá trị của chúng
    def __lt__(self, other):
        return self.val < other.val

# Hàm tiện ích để chuyển đổi từ mảng thành danh sách liên kết
def array_to_linked_list(arr: List[int]):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for num in arr[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

# Hàm tiện ích để chuyển đổi từ danh sách liên kết thành mảng


def linked_list_to_array(node: Optional[ListNode]):
    array = []
    while node:
        array.append(node.val)
        node = node.next
    return array
