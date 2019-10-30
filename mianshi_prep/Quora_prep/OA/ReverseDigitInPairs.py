def solution(num):
    strNum = list(str(num))
    for i in range(1,len(strNum),2):
        strNum[i],strNum[i-1] = strNum[i-1],strNum[i]

    return int(''.join(strNum))

print (solution(12345))
