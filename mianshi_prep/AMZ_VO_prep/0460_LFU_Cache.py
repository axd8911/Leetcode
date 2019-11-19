class Node:
    def __init__(self,key,val,freq):
        self.key = key
        self.val = val
        self.freq = freq
        self.prev = None
        self.next = None

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = {}
        self.tail = {}
        self.dic = {}
        self.freq = collections.defaultdict(set)
        self.minFreq = 0

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        oldNode = self.dic[key]
        newNode = Node(key,oldNode.val,oldNode.freq+1)
        self.dic[key] = newNode
        self.remove(oldNode)
        self.add(newNode)
        return newNode.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        exeu = False
        if len(self.dic)==self.capacity:
            exeu = True
            freq = self.minFreq
            node = self.head[freq].next

        if key in self.dic:
            oldNode = self.dic[key]
            self.remove(self.dic[key])
            newNode = Node(key,value,oldNode.freq+1)
        else:
            newNode = Node(key,value,0)
        self.dic[key] = newNode
        self.add(newNode)

        if exeu and len(self.dic)>self.capacity:
            self.remove(node)
            del self.dic[node.key]

    def add(self,node):
        freq = node.freq
        if freq not in self.head:
            self.head[freq] = Node(0,0,-1)
            self.tail[freq] = Node(0,0,-1)
            self.head[freq].next = self.tail[freq]
            self.tail[freq].prev = self.head[freq]

        p = self.tail[freq].prev
        p.next = node
        node.next = self.tail[freq]
        self.tail[freq].prev = node
        node.prev = p

        if freq>0:
            self.freq[freq].add(node.key)

        else:
            self.freq[0].add(node.key)
            self.minFreq = 0


    def remove(self,node):
        freq = node.freq
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        if n.freq == -1 and p.freq == -1:
            del self.head[freq]
            del self.tail[freq]

        self.freq[freq].remove(node.key)
        if not self.freq[freq] and freq == self.minFreq:
            self.minFreq = freq + 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
