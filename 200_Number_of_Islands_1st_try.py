class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        #把所有val==1的坐标保存在一个set里面
        #第一个点pop出来存到当前要处理的list中，检查他的上下左右是否在set里，如果是的话，进入下一轮检查，同时将这一轮的坐标放进这个island的点阵里面去
        
        ones = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    ones.add((i,j))
                
        island = 0
        
        while ones:
            island += 1
            curr = [ones.pop()]
            while curr:
                nextCheck = []
                for item in curr:
                    if (item[0]-1, item[1]) in ones:
                        nextCheck.append((item[0]-1, item[1]))
                        ones.remove((item[0]-1, item[1]))
                    if (item[0]+1, item[1]) in ones:
                        nextCheck.append((item[0]+1, item[1]))
                        ones.remove((item[0]+1, item[1]))
                    if (item[0], item[1]-1) in ones:
                        nextCheck.append((item[0], item[1]-1))
                        ones.remove((item[0], item[1]-1))
                    if (item[0], item[1]+1) in ones:
                        nextCheck.append((item[0], item[1]+1))
                        ones.remove((item[0], item[1]+1))
                #island[-1] += nextCheck
                curr = nextCheck
                
        return (island)
            
            
            
