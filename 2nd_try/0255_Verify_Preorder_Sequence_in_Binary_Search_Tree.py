class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        small = float('-inf')
        i=-1

        for p in preorder:
            if p<small:
                return False
            while i>=0 and p>preorder[i]:
                small = preorder[i]
                i-=1
            i += 1
            preorder[i] = p
        return True

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        small = float('-inf')
        for p in preorder:
            if p<small:
                return False
            while stack and p>stack[-1]:
                small = stack.pop()
            stack.append(p)
        return True
