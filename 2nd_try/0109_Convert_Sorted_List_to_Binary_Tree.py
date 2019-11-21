# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        temp = head
        cnt = 0
        while temp:
            temp = temp.next
            cnt +=1
        self.head = head
        def helper(l,r):

            if l>=r:
                return
            mid = (l+r)//2
            left = helper(l,mid)
            node = TreeNode(self.head.val)
            self.head = self.head.next
            right = helper(mid+1,r)
            node.left = left
            node.right = right
            return node
        return helper(0,cnt)
