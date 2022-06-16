from typing import List, Optional
# Definition for singly-linked list.



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        mid = self.get_mid(head)
        temp = mid.next
        mid.next = None
        left, right = self.sortList(head), self.sortList(temp)
        return self.merge_two_lists(left, right)

    def get_mid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge_two_lists(self, list1, list2):
        head = temp = ListNode(0)

        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = ListNode(list1.val)
                list1 = list1.next
            else:
                temp.next = ListNode(list2.val)
                list2 = list2.next
            temp = temp.next
        if list1:
            temp.next = list1
        else:
            temp.next = list2
        return head.next


class SortList:
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    x = Solution().sortList(head)
    print(x)
