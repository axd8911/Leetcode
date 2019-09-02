class Node:
    def __init__(self,val,neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def deepCopy(self,head):
        output = curr = Node(0,[])
        visited = set()
        exist = {}
        stack = []
        while head or stack:
            if not head:
                head = stack.pop()
            if head.val in exist:
                curr.neighbors.append(exist[head.val])
            else:
                curr.
