def bubbleSort(nums):
    # time: O(n**2), theta(n**2), omega(n)
    # space: O(1)
    for i in range(len(nums),-1,-1):
        for j in range(1,i):
            if nums[j]<nums[j-1]:
                nums[j],nums[j-1] = nums[j-1],nums[j]
    return nums

def insertionSort(nums):
    for i in range(len(nums)):
        curr = i
        while curr>0:
            if nums[curr]<nums[curr-1]:
                nums[curr],nums[curr-1] = nums[curr-1],nums[curr]
                curr-=1
            else:
                break
    return nums

def selectionSort(nums):
    loc = 0
    while loc<len(nums):
        print ('yes')
        minLoc = loc
        for i in range(minLoc,len(nums)):
            if nums[i] < nums[minLoc]:
                minLoc = i
        nums[loc],nums[minLoc] = nums[minLoc],nums[loc]
        loc += 1
    return nums

def mergeSort(nums):
    if len(nums)<=1:
        return

    mid = len(nums)//2
    L = nums[:mid]
    R = nums[mid:]
    mergeSort(L)
    mergeSort(R)

    i,j,k=0,0,0
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            nums[k] = L[i]
            i+=1
        else:
            nums[k] = R[j]
            j+=1
        k+=1
    while i<len(L):
        nums[k] = L[i]
        k+=1
        i+=1
    while j<len(R):
        nums[k] = R[j]
        k+=1
        j+=1


def quickSort(nums,low,high):
    if low>=high:
        return
    pivot = nums[high]
    pos = low

    for i in range(low,high):
        if nums[i]<pivot:
            nums[i],nums[pos]=nums[pos],nums[i]
            pos+=1
    nums[high],nums[pos] = nums[pos],nums[high]

    quickSort(nums,low,pos-1)
    quickSort(nums,pos+1,high)


if __name__ == "__main__":
    nums = [3,7,8,5,6,1,5,-2]
    res = quickSort(nums,0,len(nums)-1)
    print (nums)
