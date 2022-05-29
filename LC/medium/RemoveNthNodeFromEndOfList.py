from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        slow = fast = head

        while count < n:
            fast = fast.next
            count += 1
        if fast:
            while fast.next is not None:
                fast = fast.next
                slow = slow.next
            slow.next = slow.next.next
            return head
        else:
            return head.next


class RemoveNthNodeFromEndOfList:
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    n = int(input())
    x = Solution().removeNthFromEnd(head, n)
    print(x)
