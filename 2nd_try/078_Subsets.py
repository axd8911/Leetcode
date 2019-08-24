class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def helper(comb,res):
            output.append(comb)
            for i in range(len(res)):
                helper(comb+[res[i]],res[i+1:])

        helper([],nums)
        return output
