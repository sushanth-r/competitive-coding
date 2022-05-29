from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None, head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev


class ReverseLinkedList:
    head = ListNode(1)
    head.next = ListNode(2)
    x = Solution().reverseList(head)
    print(x)
