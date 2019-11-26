class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        visited = {(sr,sc)}
        queue = collections.deque([(sr,sc)])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        oldColor = image[sr][sc]
        h,w = len(image),len(image[0])

        while queue:
            x,y = queue.popleft()
            image[x][y] = newColor
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if 0<=nx<h and 0<=ny<w and (nx,ny) not in visited and image[nx][ny] == oldColor:

                    visited.add((nx,ny))
                    queue.append((nx,ny))

        return image
