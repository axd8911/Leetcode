'''
This is a very stupid slow approach to solve binary tree inorder question.
Only beat 5% users.
Should learn about the treatment of binary tree and solve these type of questions more smartly.

Main idea here:
- Save all "root" in a list, use None is no root
- Read the root.val and save to another list, the list order is the inorder of a full tree. remove None elements.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        rootList = []
        n = 0
        rootList.append([])
        rootList[0].append(root)
        
        
        while rootList[n] != [None for i in range(len(rootList[n]))]:
            rootList.append([])
            for item in rootList[n]:
                if item == None:
                    rootList[n+1].append(None)
                    rootList[n+1].append(None)
                else:
                    if item.left != None:
                        rootList[n+1].append(item.left)
                    if item.left == None:
                        rootList[n+1].append(None)
                    if item.right != None:
                        rootList[n+1].append(item.right)
                    if item.right == None:
                        rootList[n+1].append(None)
                    
            n = n + 1
        
        result = [None for i in range(2**len(rootList))]
        for i in range(len(rootList)):
            for j in range(len(rootList[i])):
                if rootList[i][j] != None:
                    result[2**(len(rootList)-i)*j + 2**(len(rootList)-i-1)-1] = rootList[i][j].val
                
        result = [i for i in result if i != None]
        
        return result
