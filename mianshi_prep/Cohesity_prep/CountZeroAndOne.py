# how many 0s in front and 1s in end of a item in list

def countDigit(nums):
    summation = []
    init = 0
    for item in nums:
        summation.append(init + item)
        init += item
    total = summation[-1]
    zeroCnt = []
    oneCnt = []

    for i in range(len(nums)):
        zeroCnt.append(i-summation[i]+nums[i])
        oneCnt.append(total - summation[i])

    return (zeroCnt,oneCnt)

print (countDigit([0,1,0,1,1,1,0,1,0,1]))
