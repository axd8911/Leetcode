# double side linked list
class Node:
    def __init__(self, key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key,value)
        self.dic[key] = n
        self._add(n)
        if len(self.dic)>self.capacity:
            early = self.head.next
            del self.dic[early.key]
            self._remove(early)

    def _remove(self,node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self,node):
        p = self.tail.prev
        p.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = p

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Ordered List
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.dic:
            n = self.dic[key]
            del self.dic[key]
            self.dic[key] = n
            return n
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            del self.dic[key]
        self.dic[key] = value
        if len(self.dic)>self.capacity:
            self.dic.popitem(last= False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
