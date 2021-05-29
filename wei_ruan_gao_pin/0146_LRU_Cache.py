class ListNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        self.remove(self.dic[key])
        self.add(self.dic[key])
        return self.dic[key].value
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.remove(self.dic[key])
            del self.dic[key]
        
        node = ListNode(key,value)
        self.dic[key] = node
        self.add(node)
        if len(self.dic)>self.capacity:
            to_delete = self.head.next
            del self.dic[to_delete.key]
            self.remove(to_delete)

    def add(self, node):
        p = self.tail.prev
        p.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = p

    def remove(self, node):
        n = node.next
        p = node.prev
        n.prev = p
        p.next = n

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
