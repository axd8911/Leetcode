'''
Two solutions below.
Modified solution goes up to 82%
The other is around 20-25%.

Could make the code looks simplier
.
Comments:
1.3*3 small cubes - how to represent by i and j
2. List is slow. Other's may use without list
3. for loop in for loop. any better run time level?

add up comments:
1. learned how to use enumerate()
2. 5//3 = 1, no need to use int to cast numbers

'''
#Modified solution

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        XY_set = {}  
        for (i,row) in enumerate(board):
            for (j,item) in enumerate(row):
                if item != '.':
                    if item not in XY_set:
                        XY_set.update({item:[[i,j]]})
                    else:
                        temp_set = XY_set[item]
                        if i in [ele[0] for ele in temp_set]:
                            return False
                        if j in [ele[1] for ele in temp_set]:
                            return False
                        for ele in temp_set:
                            if ele[0]//3 == i//3 and ele[1]//3 == j//3:
                                return False
                        XY_set[item] += [[i,j]]
                    
        return True
        


#other solution

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
        
        


        
