from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        stack1 = []
        node1, node2 = l1, l2
        while node1:
            stack1.append(node1.val)
            node1 = node1.next

        sum1, sum2 = 0, 0
        i = len(stack1) - 1
        while stack1:
            ele = stack1.pop()
            sum1 += ele * (10 ** i)
            i -= 1

        stack1.clear()
        while node2:
            stack1.append(node2.val)
            node2 = node2.next

        i = len(stack1) - 1
        while stack1:
            ele = stack1.pop()
            sum2 += ele * (10 ** i)
            i -= 1

        result = sum1 + sum2
        head = prev = ListNode()

        if result == 0:
            return ListNode(0)

        while result > 0:
            mod, result = result % 10, result // 10
            node = ListNode(mod)
            prev.next = node
            prev = node
        return head.next


class AddTwoNumbers:
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(8)
    x = Solution().addTwoNumbers(l1, l2)
    print(x)
