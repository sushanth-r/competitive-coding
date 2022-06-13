class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = ListNode(-1, -1)
        self.right = ListNode(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        last_node = self.right.prev
        last_node.next, node.prev = node, last_node
        node.next, self.right.prev = self.right, node

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next, next_node.prev = next_node, prev_node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = ListNode(key, value)
            self.cache[key] = node
        else:
            node = self.cache[key]
            node.value = value
            self.remove(node)
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            del self.cache[lru.key]
            self.remove(lru)


class LRUCache:
    x = LRUCache(2)
    x.put(2, 1)
    x.put(1, 1)
    x.put(2, 3)
    x.put(4, 1)
    print(x.get(1))
    print(x.get(2))
