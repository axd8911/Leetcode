'''
Two solutions below.
Both are around 20-25%.

Slightly away from main fastest range
Should come back and check other's solutions
.
Comments:
1.3*3 small cubes - how to represent by i and j
2. List is slow. Other's may use without list
3. for loop in for loop. any better run time level?
'''

#solution 1

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            temp_list = []
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in temp_list:
                    return False
                if board[i][j] != '.':
                    temp_list.append(board[i][j])                    

            temp_list = []    
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in temp_list:
                    return False
                if board[j][i] != '.':
                    temp_list.append(board[j][i])  
                    
            temp_list = []
            for j in range(9):
                
                if board[j%3+(i-i%3)][int(j/3)+(i%3)*3] != '.' and board[j%3+(i-i%3)][int(j/3)+(i%3)*3] in temp_list:
                    return False
                if board[j%3+(i-i%3)][int(j/3)+(i%3)*3] != '.':
                    temp_list.append(board[j%3+(i-i%3)][int(j/3)+(i%3)*3])  
                                
        return True
        
        
#solution2

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        XY_set = {}
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] >'0' and board[i][j]<='9':
                    if board[i][j] not in XY_set:
                        XY_set.update({board[i][j]:[[i,j]]})
                    else:
                        temp_set = XY_set[board[i][j]]
                        if i in [item[0] for item in temp_set]:
                            return False
                        if j in [item[1] for item in temp_set]:
                            return False
                        for item in temp_set:
                            if int(item[0]/3) == int (i/3) and int(item[1]/3) == int (j/3):
                                return False
                    XY_set[board[i][j]] = XY_set[board[i][j]] + [[i,j]]
                    
                    
        return True
        
