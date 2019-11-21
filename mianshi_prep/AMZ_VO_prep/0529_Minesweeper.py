class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        a,b = click
        if board[a][b] == 'M':
            board[a][b] = 'X'
            return board

        h,w = len(board),len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]

        visited = {(a,b)}
        queue = collections.deque([(a,b)])
        while queue:
            x,y = queue.popleft()
            num = 0
            for dx,dy in directions:
                newX,newY = x+dx,y+dy
                if 0<=newX<h and 0<=newY<w and board[newX][newY]=='M':
                    num += 1

            if num>0:
                board[x][y] = str(num)
            else:
                board[x][y] = 'B'
                for dx,dy in directions:
                    newX,newY = x+dx,y+dy
                    if 0<=newX<h and 0<=newY<w and (newX,newY) not in visited:
                        visited.add((newX,newY))
                        queue.append((newX,newY))

        return board
