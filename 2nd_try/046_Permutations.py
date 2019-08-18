class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        length = len(nums)

        def bt(comb,nums):
            print (comb)
            if len(comb) == length:
                output.append(comb)
                return

            for i in range(len(nums)):
                bt(comb+[nums[i]],nums[:i]+nums[i+1:])

        bt([],nums)
        return output
