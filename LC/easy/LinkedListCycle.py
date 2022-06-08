from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # O(n) - Time & O(n) - Space
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        temp = head
        while temp is not None:
            if temp in visited:
                return True
            visited.add(temp)
            temp = temp.next
        return False

    def hasCycleV2(self, head: Optional[ListNode]) -> bool:
        # O(n) - Time & O(n) - Space
        if not head or not head.next:
            return False

        slow = head.next
        fast = head.next.next

        while slow and fast:
            if slow == fast:
                return True
            slow = slow.next

            if not fast.next:
                return False
            fast = fast.next.next

        return False


class LinkedListCycle:
    head = ListNode(3)
    head.next = ListNode(2)
    # head.next.next = ListNode(0)
    # head.next.next.next = ListNode(-4)
    # head.next.next.next.next = head.next
    x = Solution().hasCycleV2(head)
    print(x)
