# get:
# put:

class Node:
    def __init__(self,key,value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class Solution:
    def __init__(self,capacity):
        self.dic = {}
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self,key):
        if key not in dic:
            return -1
        new = Node(key,self.dic[key])
        delete(self.dic[key])       # delete the old node
        add(new)
        return new.val

    def put(self,key,value):
        if key in self.dic:
            delete(self.dic[key])
        self.dic[key] = value
        new = Node(key,value)
        add(new)
        if len(self.dic)>self.capacity:
            extra = head.next.key
            del self.dic[extra]
            delete(head.next)



    def delete(self,node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def add(self,node):
        p = tail.prev
        p.next = node
        node.next = tail
        tail.prev = node
        node.prev = p
