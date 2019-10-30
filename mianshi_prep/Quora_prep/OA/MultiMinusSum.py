def solution(myNum):
    summation = 0
    product = 1
    while myNum:
        curr = myNum%10
        myNum//=10
        summation += curr
        product *= curr
    return product-summation

num = 12345
print (solution(num))
