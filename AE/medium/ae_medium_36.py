# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def detach_node(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node
        if self.head == node:
            self.head = next_node
        if self.tail == node:
            self.tail = prev_node

    def setHead(self, node: Node):
        previous_head = self.head
        if not previous_head:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node: Node):
        previous_tail = self.tail
        if not previous_tail:
            self.head = node
            self.tail = node
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node: Node, node_to_insert: Node):
        self.detach_node(node_to_insert)

        prev_node = node.prev
        node_to_insert.next = node
        node.prev = node_to_insert
        if prev_node:
            prev_node.next = node_to_insert
            node_to_insert.prev = prev_node
        else:
            self.head = node_to_insert

    def insertAfter(self, node, node_to_insert):
        self.detach_node(node_to_insert)

        next_node = node.next
        node.next = node_to_insert
        node_to_insert.prev = node
        if next_node:
            node_to_insert.next = next_node
            next_node.prev = node_to_insert
        else:
            self.tail = node_to_insert

    def insertAtPosition(self, position, node_to_insert):
        self.detach_node(node_to_insert)

        node = self.head
        start = 1
        while start < position:
            node = node.next
            start += 1
        prev_node = node.prev
        node_to_insert.prev = prev_node
        if prev_node:
            prev_node.next = node_to_insert
            node_to_insert.next = node
        if self.head == node:
            self.head = node_to_insert

    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                prev_node = node.prev
                next_node = node.next
                if prev_node:
                    prev_node.next = next_node
                if next_node:
                    next_node.prev = prev_node
                if self.head == node:
                    self.head = node.next
                if self.tail == node:
                    self.tail = node.prev
            node = node.next

    def remove(self, node):
        self.detach_node(node)

    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                return True
            node = node.next
        return False


class LinkedListConstruction:
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    # one.next = two
    # two.prev = one
    # two.next = three
    # three.prev = two
    linked_list = DoublyLinkedList()
    linked_list.setHead(five)
    linked_list.setHead(four)
    linked_list.setHead(three)
    linked_list.setHead(two)
    linked_list.setHead(one)
    linked_list.setHead(four)
    linked_list.setTail(six)
    # linked_list.head = one
    # linked_list.tail = three
    # linked_list.insertBefore(two, four)
    print(linked_list)
