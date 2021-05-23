class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        output = []
        curr = []
        for i in range(len(nums)):
            for j in range(len(output)):
                if nums[i] >= output[j][-1]:
                    output.append(output[j][:]+[nums[i]])
            output.append([nums[i]])

        return set(tuple(item) for item in output if len(item)>1)
