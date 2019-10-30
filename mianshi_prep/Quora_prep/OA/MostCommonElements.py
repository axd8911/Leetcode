import collections

def solution(nums):
    output = []
    dic = collections.Counter(nums)
    most = max(dic.values())
    for item in dic:
        if dic[item]==most:
            output.append(item)
    return output

if __name__ == "__main__":
    nums = [2,2,3,4,3,5]
    print (solution(nums))
