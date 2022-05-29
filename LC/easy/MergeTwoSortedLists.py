# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        result = ListNode()
        node = result

        while list1 and list2:
            if list1.val <= list2.val:
                node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                node.next = ListNode(list2.val)
                list2 = list2.next
            node = node.next

        if not list1:
            node.next = list2
        else:
            node.next = list1
        return result.next


class MergeTwoSortedLists:
    list1 = ListNode(1)
    list1.next = ListNode(6)

    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(5)
    x = Solution().mergeTwoLists(list1, list2)
    print(x)
