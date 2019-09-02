# a list of numbers small -> large -> small. Find the Largest
class Solution:
    def findLargest(self,nums):
        start = 0
        end = len(nums)-1
        while start<=end:
            mid = (start+end)//2
            if mid +1 < len(nums) and nums[mid] < nums[mid+1]:
                start = mid+1
            else:
                end = mid-1
        return nums[start]
def main():
    nums = [5,7]
    a = Solution().findLargest(nums)
    print (a)
main()
