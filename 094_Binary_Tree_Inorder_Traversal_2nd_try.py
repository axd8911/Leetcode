'''
99.73%

Look over all items, more practice
'''

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        self.output = []
        
        def inorder(root):
            if root: 
                inorder(root.left)
                self.output.append(root.val)
                inorder(root.right)
        
        if root:
            inorder(root)
            
        return self.output
