import collections

def solution(a,b):
    countA = collections.Counter(list(a))
    countB = collections.Counter(list(b))
    return set(countA.keys()) == set(countB.keys()) and list(countA.values()).sort() == list(countB.values()).sort()

a = 'babzcccm'
b = 'bbazzczm'
print (solution(a,b))
