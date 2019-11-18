class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        line = []

        for i in range(len(board)-1,-1,-1):
            if (len(board)-i)%2==1:
                for j in range(len(board[i])):
                    if board[i][j] !=-1:
                        line.append(board[i][j]-1)
                    else:
                        line.append(-1)

            else:
                for j in range(len(board[i])-1,-1,-1):
                    if board[i][j] !=-1:
                        line.append(board[i][j]-1)
                    else:
                        line.append(-1)
        self.cnt = float('inf')
        size = len(line)
        visited = set()

        step = 0
        curr = collections.deque([0])
        while curr:
            length = len(curr)
            step += 1
            for i in range(length):
                item = curr.popleft()

                for j in range(1,7):
                    if  item+j<size:
                        if item+j not in visited and line[item+j]==-1:
                            curr.append(item+j)
                            visited.add(item+j)
                        elif line[item+j] not in visited and line[item+j]!=-1:
                            curr.append(line[item+j])
                            visited.add(line[item+j])
                        if size-1 in visited:
                            return step

        return -1

            
