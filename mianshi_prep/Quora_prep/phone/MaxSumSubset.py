# a list with numbers, find the maximum sum where no two numbers are adjancent
import collections
def solution(nums):
    dic = collections.defaultdict(int)
    for item in nums:
        dic[item] += item

    keepThis,keepLast = 0,0
    myKeys = sorted(list(dic.keys()))

    for item in myKeys:
        if item-1 in myKeys:
            keepThis,keepLast = keepLast + dic[item], keepThis

        else:
            keepThis = max(keepLast,keepThis) + dic[item]
    return max(keepThis,keepLast)

nums = [3,2,1,3,2,2,2,1,2,5,5]
print (solution(nums))
