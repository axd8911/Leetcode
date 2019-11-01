class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        start,dest = tuple(start),tuple(destination)
        curr = collections.deque([start])
        visited = set(start)
        h,w = len(maze),len(maze[0])

        while curr:
            x,y = curr.popleft()
            xup,xdown = x,x
            yup,ydown = y,y

            while xup-1>=0 and maze[xup-1][y] == 0:
                xup-=1
            while xdown+1 < h and maze[xdown+1][y] == 0:
                xdown +=1
            while yup-1>=0 and maze[x][yup-1] == 0:
                yup-=1
            while ydown+1 < w and maze[x][ydown+1] == 0:
                ydown +=1

            for item in [(xup,y),(xdown,y),(x,yup),(x,ydown)]:
                if item not in visited:
                    if item == dest:
                        return True
                    visited.add(item)
                    curr.append(item)

        return False
