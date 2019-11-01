# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # summation values till now: currSum minus any of them results in SUM, that's good

        def dfs(root,currSum):
            if not root:
                return 0
            cnt = 0
            currSum += root.val

            if currSum - sum in dic:
                cnt += dic[currSum-sum]
            dic[currSum] += 1
            cnt += dfs(root.left,currSum)
            cnt += dfs(root.right,currSum)
            dic[currSum] -= 1
            return cnt
        dic = collections.defaultdict(int)
        dic[0] = 1
        return dfs(root,0)

    # dic[currSum] should come later because 算当前位置的情况， 不能考虑截至当前位置所有数字的和（currSum) 减去 截至当前位置所有数字的和（这里不正确的多加了一个和）
    # dic[0] = 1 should be there because 当然有一种和是什么都没有，这样才能考虑从root到某个位置的全局

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:

        # record the possible summations on each node
        if not root:
            return 0

        stack = []
        total = 0
        oldSum = {}

        while stack or root:
            while root:
                #print ('old： ', root.val,oldSum)
                newSum = {key+root.val:oldSum[key] for key in oldSum}
                if root.val in newSum:
                    newSum[root.val] += 1
                else:
                    newSum[root.val] = 1

                if sum in newSum:
                    total += newSum[sum]

                stack.append((root,newSum))
                root = root.left
                oldSum = newSum

            root,oldSum = stack.pop()
            root = root.right

        return total
