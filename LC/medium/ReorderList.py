# Definition for singly-linked list.
import math
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr = []
        node = head
        while node is not None:
            arr.append(node)
            node = node.next

        i, j = 0, len(arr) - 1
        k = 0
        while k < math.floor(len(arr) / 2):
            arr[i].next = arr[j]
            arr[j].next = arr[i + 1]
            i += 1
            j -= 1
            k += 1
        arr[i].next = None


class ReorderList:
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    # head.next.next.next.next.next = ListNode(6)
    Solution().reorderList(head)
    print(head)
