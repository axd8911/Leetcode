'''
Leetcode.com gives score of 70%, which is fine. Space usage is a bit high because of those redundent lists
In this first try, I am trying to understanding trees operation and these link list
I used a lot of 'if's to achieve the boundary situations.
After more practices, I need to come back and simplify the code


'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        judge = False
        p_list = [p]
        q_list = [q]
        if p_list == [None] and q_list == [None]:
            judge = True
                
        while p_list != [None]*len(p_list) and q_list != [None]*len(p_list):
            judge = True          
            
            if [p_list[i].val for i in range(len(p_list))] != [q_list[i].val for i in range(len(q_list))]:
                judge = False
                break            
            
            if len([x.left for x in p_list if x.left is not None]) != len([x.left for x in q_list if x.left is not None]):
                judge = False
                break
                
            if len([x.right for x in p_list if x.right is not None]) != len([x.right for x in q_list if x.right is not None]):
                judge = False
                break
            
            p_list = [x.left for x in p_list if x.left is not None] + [x.right for x in p_list if x.right is not None]
            q_list = [x.left for x in q_list if x.left is not None] + [x.right for x in q_list if x.right is not None]
            
        return judge
        
        

        
