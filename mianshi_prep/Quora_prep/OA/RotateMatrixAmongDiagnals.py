# if location in diagnals, do not move
# else, do some math in x and y

def solution(matrix,k):
    h = len(matrix)
    w = len(matrix[0])
    if h!=w:
        return
    if k==4:
        return matrix

    newMat = [[0 for i in range(h)] for j in range(h)]

    for i in range(h):
        for j in range(h):
            if i+j == h-1 or i == j:
                newMat[i][j] = matrix[i][j]
            else:
                if k==1:
                    newMat[j][h-1-i] = matrix[i][j]
                elif k==2:
                    newMat[h-1-i][h-1-j] = matrix[i][j]
                elif k==3:
                    newMat[h-1-j][i] = matrix[i][j]


    return newMat

if __name__ == "__main__":
    matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    print (solution(matrix,3))
