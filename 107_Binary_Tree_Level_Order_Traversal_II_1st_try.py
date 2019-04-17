'''
74%
This question is in BFS catagoroy. Here I just used lists in list solution. Should try it in next try.
'''

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        
        nodelist = [[root]]
        vals = [[root.val]]
        n = 0
        while nodelist[-1] != []:
            nodelist.append([])
            vals.append([])
            for node in nodelist[n]:
                if node.left != None:
                    nodelist[n+1].append(node.left)
                    vals[n+1].append(node.left.val)
                if node.right != None:
                    nodelist[n+1].append(node.right)
                    vals[n+1].append(node.right.val)
            n = n + 1
        
        del vals[-1]
        
        return vals[::-1]
        

        
        
 
