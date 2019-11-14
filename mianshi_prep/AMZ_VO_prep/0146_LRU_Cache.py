class Node:
    def __init__(self,key,val):
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
        if key not in self.dic:
            return -1

        self._delete(self.dic[key])
        self._add(self.dic[key])
        return self.dic[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self._delete(self.dic[key])

        self.dic[key] = Node(key,value)
        self._add(self.dic[key])
        if len(self.dic)>self.capacity:
            outIndex = self.head.next.key
            self._delete(self.dic[outIndex])
            del self.dic[outIndex]

    def _delete(self,node):
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
