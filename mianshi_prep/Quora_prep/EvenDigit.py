def solution(nums):
    output = 0
    for num in nums:
        while num:
            curr = num%10
            if not curr%2:
                output +=1
                break
            num//=10
    return output

nums = [12,3,4,5,3456]
if __name__ == "__main__":
    print (solution(nums))
