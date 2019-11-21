class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

        sx,sy = start
        dx,dy = destination
        if maze[sx][sy]==1 or maze[dx][dy]==1:
            return -1

        h = len(maze)
        w = len(maze[0])

        queue = collections.deque([[sx,sy]])
        dic = collections.defaultdict(int)
        dic[(sx,sy)] = 0
        visited = set()
        updated = True

        while updated:
            updated = False
            #print (queue)
            length = len(queue)
            for i in range(length):
                x,y = queue.popleft()
                copyDic = dic
                xup,xdown = x,x
                yup,ydown = y,y
                while xup-1>=0 and maze[xup-1][y]!=1:
                    xup-=1
                while xdown+1<h and maze[xdown+1][y]!=1:
                    xdown+=1
                while yup-1>=0 and maze[x][yup-1]!=1:
                    yup-=1
                while ydown+1<w and maze[x][ydown+1]!=1:
                    ydown+=1

                for nx,ny in [[xup,y],[xdown,y],[x,yup],[x,ydown]]:
                        newDistance = dic[(x,y)] + abs(nx-x) + abs(ny-y)
                        if (nx,ny) not in visited or dic[(nx,ny)]>newDistance:
                            #print ('yes')
                            updated = True
                            dic[(nx,ny)] = newDistance
                            visited.add((nx,ny))
                            queue.append([nx,ny])

        if (dx,dy) in visited:
            return dic[(dx,dy)]
        return -1
