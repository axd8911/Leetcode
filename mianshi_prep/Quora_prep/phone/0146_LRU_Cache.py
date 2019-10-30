class Node:
    def __init__(self,key,val):
        self.val = val
        self.key = key
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
            self._rem(n)
            self._add(n)
            return n.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self._rem(self.dic[key])
        n = Node(key,value)
        self.dic[key] = n
        self._add(n)
        if len(self.dic)>self.capacity:
            early = self.head.next
            self._rem(self.dic[early.key])
            del self.dic[early.key]

    def _add(self,node):
        p = self.tail.prev
        p.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = p


    def _rem(self,node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
