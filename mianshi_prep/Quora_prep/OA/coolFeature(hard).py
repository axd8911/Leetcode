
import collections
def solution(a,b,query):

    dicA = collections.Counter(a)
    dicB = collections.Counter(b)

    def findValue(A,B,target):
        print (A,B)
        total = 0
        for item1 in A:
            if target-item1 in B:
                total += A[item1] * B[target-item1]
        return total

    output = []
    for q in query:
        if q[0] == 0:
            output.append(findValue(dicA,dicB,q[1]))
        elif q[0] == 1:
            dicB[b[q[1]]] -= 1
            b[q[1]] = q[2]
            dicB[b[q[1]]] += 1

    return output

a = [1,2,3]
b = [3,4]
query = [[0, 5], [1, 1 , 1], [0, 5]]
print (solution(a,b,query))
