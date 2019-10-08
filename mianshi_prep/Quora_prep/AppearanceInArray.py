
import collections
def solution(a,query):
    dic = collections.defaultdict(list)
    for item in query:
        dic[item[2]].append((item[0],item[1]))
    print (dic)
    total = 0
    for i in range(len(a)):
        if a[i] in dic:
            for interval in dic[a[i]]:
                print (interval)
                if interval[0]<=i<=interval[1]:
                    total += 1
    return total

if __name__ == "__main__":
    a = [1,1,2,3,2]
    matrix = [[1,2,1],[2,4,2],[0,3,1]]
    print (solution(a,matrix))
