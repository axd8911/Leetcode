'''
20%
Need to rework and cut off the time-eating codes
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """        
        invalid = {}
        
        for i in range(1,len(board)-1):
            for j in range(1,len(board[i])-1):
                if board[i][j] == 'O' and (i,j) not in invalid:
                    
                    warning = False
                    O_set = {(i,j):None}
                    O_dict = {(i,j):None}
                    while O_set != {}:
                        new = {}
                        for key in O_set:
                            if key[1]-1>= 0 and board[key[0]][key[1]-1] == 'O' and (key[0],key[1]-1) not in O_dict:
                                new[(key[0],key[1]-1)] = None
                            if key[1]+1<= len(board[i])-1 and board[key[0]][key[1]+1] == 'O' and (key[0],key[1]+1) not in O_dict:
                                new[(key[0],key[1]+1)] = None
                            if key[0]-1>= 0 and board[key[0]-1][key[1]] == 'O' and (key[0]-1,key[1]) not in O_dict:
                                new[(key[0]-1,key[1])] = None
                            if key[0]+1<= len(board)-1 and board[key[0]+1][key[1]] == 'O' and (key[0]+1,key[1]) not in O_dict:
                                new[(key[0]+1,key[1])] = None
                        O_dict.update(new)
                        O_set = new

                    for key in O_dict:
                        if key[0] == 0 or key[0] == len(board)-1 or key[1] == 0 or key[1] == len(board[i])-1:
                            warning = True
                            break
                    if warning == True:
                        invalid.update(O_dict)
                    else:
                        for key in O_dict:
                            board[key[0]][key[1]] = 'X'


                        
                
