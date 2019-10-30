import collections
def solution(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = -1

    prefix = [0]
    total = 0
    for item in nums:
        total+=item
        prefix.append(total)

    dic = collections.defaultdict(list)
    for i in range(len(prefix)):
        dic[prefix[i]].append(i)
    largest = 0
    for key in dic:
        largest = max(largest,dic[key][-1]-dic[key][0])
    print (prefix)
    return largest

nums = [0,0,1,1,1,0,0,1]
print (solution(nums))
