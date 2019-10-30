def solution(n,k):
    curr = n
    div = 10**k
    total = set()
    while curr>=div/10:
        print ('curr ',curr)
        item = curr%div
        curr //= 10
        print (item)
        if not n%item:
            total.add(item)

    return len(total)

if __name__ == "__main__":
    n = 555
    k = 1
    print (solution(n,k))
