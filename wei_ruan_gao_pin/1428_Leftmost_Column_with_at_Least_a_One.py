# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        row,col = binaryMatrix.dimensions()
        move_row,move_col = 0,col-1
        while True:
            while move_col>=0 and binaryMatrix.get(move_row,move_col)==1:
                move_col-=1
            move_row+=1
            if move_col==-1 or move_row==row:
                break
        return move_col+1 if move_col+1 != col else -1
