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
        self.dic = {}
        self.head = {}
        self.tail = {}
        self.minFreq = 0

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1

        freq = self.dic[key].freq
        self.delete(self.dic[key])
        self.dic[key].freq += 1
        self.add(self.dic[key])

        if self.minFreq == freq and freq not in self.head:
            self.minFreq += 1
        return self.dic[key].val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.dic:
            freq = self.dic[key].freq + 1
            self.delete(self.dic[key])
            del self.dic[key]
        else:
            freq = 0

        if len(self.dic) == self.capacity:
            least = self.head[self.minFreq].next
            self.delete(least)
            del self.dic[least.key]


        node = Node(key,value,freq)
        self.add(node)
        self.dic[key] = node

        if freq == 0:
            self.minFreq = 0

        elif freq - 1 == self.minFreq and self.minFreq not in self.head:
            self.minFreq = freq

    def add(self,node):
        freq = node.freq
        if freq not in self.head:
            self.head[freq] = Node(0,0,0)
            self.tail[freq] = Node(0,0,0)
            self.head[freq].next = self.tail[freq]
            self.tail[freq].prev = self.head[freq]

        p = self.tail[freq].prev
        p.next = node
        node.next = self.tail[freq]
        self.tail[freq].prev = node
        node.prev = p


    def delete(self,node):
        freq = node.freq
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

        if self.head[freq].next == self.tail[freq]:
            del self.head[freq]
            del self.tail[freq]




# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
