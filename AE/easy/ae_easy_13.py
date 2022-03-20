# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linked_list: LinkedList):
    current_node = linked_list
    next_potential_distinct_node = linked_list.next
    while next_potential_distinct_node is not None:
        if next_potential_distinct_node.value == current_node.value:
            next_potential_distinct_node = next_potential_distinct_node.next
        else:
            current_node.next = next_potential_distinct_node
            current_node = next_potential_distinct_node
            next_potential_distinct_node = next_potential_distinct_node.next
    current_node.next = None
    return linked_list


class DupeLinkedList:
    head = LinkedList(1)
    head.next = LinkedList(1)
    head.next.next = LinkedList(3)
    head.next.next.next = LinkedList(4)
    head.next.next.next.next = LinkedList(4)
    head.next.next.next.next.next = LinkedList(5)
    head.next.next.next.next.next.next = LinkedList(6)
    head.next.next.next.next.next.next.next = LinkedList(7)
    actual = removeDuplicatesFromLinkedList(head)
    print(actual)
