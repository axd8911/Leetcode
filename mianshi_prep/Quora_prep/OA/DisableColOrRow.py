def solution(matrix,query):
    col = [i for i in range(1,len(matrix)+1)]
    row = [i for i in range(1,len(matrix[0])+1)]
    res = []
    for item in query:
        if item[0] == 0:
            for item in col:
                if item>0:
                    factor1 = item
                    break
            for item in row:
                if item>0:
                    factor2 = item
                    break
            res.append(factor1*factor2)
        elif item[0] == 1:
            row[item[1]] = -1
        elif item[0] == 2:
            col[itme[1]] = -1

    return res
