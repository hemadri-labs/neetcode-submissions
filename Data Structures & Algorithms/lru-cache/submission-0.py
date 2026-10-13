class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value;
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.least, self.most = Node(0,0), Node(0,0)
        self.least.next = self.most
        self.most.prev = self.least
    
    def removeLeast(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insertMost(self, node):
        prev = self.most.prev
        prev.next = node
        node.prev = prev
        node.next = self.most
        self.most.prev = node 

    def get(self, key: int) -> int:
        if key in self.cache:
            self.removeLeast(self.cache[key])
            self.insertMost(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeLeast(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insertMost(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.least.next
            self.removeLeast(lru)
            del self.cache[lru.key]

        
