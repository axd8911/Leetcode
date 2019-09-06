class Node:
    def __init__(self,value):
        self.val = value
        self.next = None
        self.random = None

class Solution:
    def deepCopy(self,head):
        # visited or not
        # has random or not
        # if some node not visited: go!
        # if some node has random: save next to stack
        # copy head itself
        # if there is a random, if random in dic, connect it, else, create it
        curr = output = Node(0)
        dic = {}
        while head:
            if head.val not in dic:
                new = Node(head.val)
                dic[head.val] = new
                curr.next = new
            else:
                curr.next = dic[head.val]

            if head.random:
                if head.random.val not in dic:
                    new = Node(head.random.val)
                    dic[head.random.val] = new
                    curr.next.random = new
                else:
                    curr.next.random = dic[head.random.val]

            head = head.next
            curr = curr.next
        return output.next
