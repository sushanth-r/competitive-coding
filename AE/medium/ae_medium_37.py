# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def get_linked_list_length(head: LinkedList):
    length = 0
    node = head
    while node:
        length += 1
        node = node.next
    return length


def removeKthNodeFromEnd(head: LinkedList, k: int):
    length = get_linked_list_length(head)
    node = head
    prev_node = None
    if k == length:
        node.value = node.next.value
        node.next = node.next.next
        return

    prev_node = None
    difference = length - k
    for i in range(difference):
        prev_node = node
        node = node.next
    prev_node.next = node.next


class RemovedKthNodeFromEnd:
    zero = LinkedList(0)
    one = LinkedList(1)
    two = LinkedList(2)
    three = LinkedList(3)
    # four = LinkedList(4)
    # five = LinkedList(5)
    # six = LinkedList(6)
    # seven = LinkedList(7)
    # eight = LinkedList(8)
    # nine = LinkedList(9)
    zero.next = one
    one.next = two
    two.next = three
    # three.next = four
    # four.next = five
    # five.next = six
    # six.next = seven
    # seven.next = eight
    # eight.next = nine
    k = 4
    removeKthNodeFromEnd(zero, k)
    x = 3
