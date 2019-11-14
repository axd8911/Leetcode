# find kth missing number in a list
# check if left has enough slot, if not, go right
# it is like find the kth slot

def findMissing(nums,k):
    start = 0
    end = len(nums)-1

    while start<=end:
        #print (start, end, nums[start], nums[end], k)
        mid = (start + end)//2
        #print (k - (nums[mid]-nums[start]-(mid-start)),nums[mid+1]-nums[mid]+1)
        if mid<len(nums)-1 and 0< k - (nums[mid]-nums[start]-(mid-start))  <nums[mid+1]-nums[mid]:
            return nums[mid] + k - (nums[mid]-nums[start]-(mid-start))

        if k <= (nums[mid]-nums[start]-(mid-start)):
            #print ('yes1')
            end = mid
        else:
            #print ('yes2')
            k -= (nums[mid]-nums[start]-(mid-start))
            start = mid



nums = [2,4]
k = 1
print (k, findMissing(nums,k))
