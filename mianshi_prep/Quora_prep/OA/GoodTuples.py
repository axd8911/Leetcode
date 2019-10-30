
import collections
def solution(arr):
    if len(arr)<3:
        return 0
    output = 0

    curr = collections.deque()
    for i in range(len(arr)):
        curr.append(arr[i])
        if len(curr)==4:
            curr.popleft()
        if len(curr)==3 and (curr[0]==curr[1] or curr[1]==curr[2] or curr[2]==curr[0]):
            output += 1
    return output

if __name__ == "__main__":
    arr = [1,1,2,1,5,3,2,3]
    print (solution(arr))
