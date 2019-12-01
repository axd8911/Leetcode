def bubbleSort(nums):
    for i in range(len(nums),-1,-1):
        for j in range(1,i):
            if nums[j]<nums[j-1]:
                nums[j],nums[j-1] = nums[j-1],nums[j]

    return nums


if __name__ == "__main__":
    nums = [3,7,8,6,1,5,-2]
    res = bubbleSort(nums)
    print (res)
