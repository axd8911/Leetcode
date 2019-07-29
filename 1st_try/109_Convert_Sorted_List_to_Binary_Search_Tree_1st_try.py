'''
98.81%
'''

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
        
        allData = []
        while head:
            allData.append(head.val)
            head = head.next
        
        def dfs(allData):
            loc = len(allData)//2
            if allData:
                root = TreeNode(allData[loc])
                left = allData[:loc]
                right = allData[loc+1:]
                root.left = dfs(left)
                root.right = dfs(right)
                return root
        
        if not allData:
            return []
        else:
            return dfs(allData)
        
