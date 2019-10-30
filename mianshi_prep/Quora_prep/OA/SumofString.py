def solution(a,b):
    output = ''
    for i in range(len(a)):
        output+=str(int(a[i])+int(b[i]))

    return output

if __name__ == "__main__":
    a = '99910'
    b = '99901'
    print (solution(a,b))
