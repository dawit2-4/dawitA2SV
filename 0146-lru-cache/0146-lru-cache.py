class Node:
    def __init__(self, key, value):
        self.key, self.value =  key, value
        self.next, self.prev = None, None
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.right = Node(0, 0)
        self.left = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next, node.prev = node, prev
        node.next, next.prev = next, node
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
# Usage:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
