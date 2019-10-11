import collections
def solution(log):

    # sort the log, time - item
    # {time: {item:appearance}}
    # item: importance

    log.sort()
    print(log)
    start = log[0][0]
    end = log[-1][0]
    appears = [collections.defaultdict(int) for i in range(end-start+1)]
    for item in log:
        appears[item[0]-start][item[1]]+=1

    priority = collections.defaultdict(int)
    for appear in appears:
        for item in appear:
            priority[item] += 2*appear[item]
        for item in priority:
            if item not in appear:
                priority[item] -= 1
                if priority[item] < 0:
                    priority[item] = 0
        print (priority)
    res = []
    for key in priority:
        if priority[key]>5:
            res.append(key)
    return res

log = [[6,2],[2,1],[4,2],[1,1],[5,2],[2,1],[6,2],[7,2],[8,2],[9,2]]
print (solution(log))
