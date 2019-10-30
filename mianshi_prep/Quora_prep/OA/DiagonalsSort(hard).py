def solution(matrix):
    dim = len(matrix)
    prepMat = [[] for i in range(dim*2-1)]
    print (prepMat)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            prepMat[i-j+dim-1].append(matrix[i][j])
    for i in range(len(prepMat)):
        prepMat[i].sort()


    print (prepMat)
    output = [[0 for i in range(dim)] for j in range(dim)]
    for i in range(len(prepMat)//2):
        for j in range(len(prepMat[i])):
            output[j][j-i+dim-1] = prepMat[i][j]
            print ('1',output)
    for i in range(len(prepMat)//2,len(prepMat)):
        for j in range(len(prepMat[i])):
            output[i+j-dim+1][j] = prepMat[i][j]
            print ('2',output)
    return output

matrix = [[8,4,1],[4,4,1],[4,8,9]]
print (solution(matrix))
