def solution(a,b):
    # check the min difference in a
    # list out all possible differences
    # iterate start numbers (should be <= a[0])

    diffSet = set()
    if len(a)>1:
        diff = min([a[i]-a[i-1] for i in range(1,len(a))])
        while diff == int(diff):
            diffSet.add(diff)
            diff/=2
    print (diffSet)
    allItem = sorted(a+b)
    allSet = set(allItem)
    Aset = set(a)
    longest = -1
    for i in range(len(allItem)):
        for j in range(i+1,len(allItem)):
            curr = set()
            if not diffSet or (diffSet and (allItem[j]-allItem[i]) in diffSet):
                difference = allItem[j] - allItem[i]
                curr.add(allItem[i])
                curr.add(allItem[j])
                value = allItem[j] + difference
                while value in allSet:
                    curr.add(value)
                    value += difference
                if Aset.issubset(curr) and len(curr) > longest:
                    longest = len(curr)
    return longest


if __name__ == "__main__":
    a = [0,4,8,20]
    b = [2,5,6,7,10,12,14,16,18,22]
    print (solution(a,b))
