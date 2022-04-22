# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linked_list_one, linked_list_two):
    linked_list_sum = 0

    node = linked_list_one
    exponent = 0
    while node is not None:
        linked_list_sum += ((10 ** exponent) * node.value)
        exponent += 1
        node = node.next

    node = linked_list_two
    exponent = 0
    while node is not None:
        linked_list_sum += ((10 ** exponent) * node.value)
        exponent += 1
        node = node.next
    temp = linked_list_sum
    result = LinkedList(temp % 10)
    temp_list = result
    temp = temp // 10
    while temp > 0:
        modulus = temp % 10
        temp_list.next = LinkedList(modulus)
        temp_list = temp_list.next
        temp = temp // 10
    return result


class SumOfLinkedLists:
    linked_list_one = LinkedList(1)
    linked_list_one.next = LinkedList(3)
    linked_list_one.next.next = LinkedList(5)
    linked_list_two = LinkedList(2)
    linked_list_two.next = LinkedList(4)
    linked_list_two.next.next = LinkedList(6)
    print(sumOfLinkedLists(linked_list_one, linked_list_two))
