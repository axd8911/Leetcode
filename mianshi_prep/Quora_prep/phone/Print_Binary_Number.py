def solution(num):
    return str(bin(num+1))[3:]

myNums = [0,1,2,3,4,5,6,7,20,50]

for i in myNums:
    print (i,solution(i))
