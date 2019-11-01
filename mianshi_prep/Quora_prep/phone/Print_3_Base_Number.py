# first 3, next 9, next 27, next 81 ,...
# which range is current number in?

def solution(num):
    n = 1
    curr = num-1
    digits = 1
    while curr>=3**n:
        curr -= 3**n
        n+=1
        digits += 1
    res = []
    #num = curr
    while curr>0:
        res.append(str(curr%3))
        curr//=3
    res = res[::-1]
    res = ['0']*(digits-len(res)) + res
    return ''.join(res)

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]

for item in range(1,20):
    print(item,solution(item))
