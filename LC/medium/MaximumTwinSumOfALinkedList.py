# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp

        result = 0
        while prev:
            result = max(result, head.val + prev.val)
            head = head.next
            prev = prev.next
        return result


class MaximumTwinSumOfALinkedList:
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    x = Solution().pairSum(head)
    print(x)
