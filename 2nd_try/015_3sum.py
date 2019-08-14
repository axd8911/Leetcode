class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        match = []
        for i in range(len(nums)-2):
            if nums[i] >0:
                break
            if i>=1 and nums[i] == nums[i-1]:
                continue
            rest = -1 * nums[i]
            l,r = i+1, len(nums)-1
            while l < r:
                curr = nums[l] + nums[r]
                if curr > rest:
                    r -= 1
                elif curr < rest:
                    l += 1
                else:
                    match.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l+=1
                    while l<r and nums[r] == nums[r-1]:
                        r-=1

                    l += 1
                    r-=1

        return match
