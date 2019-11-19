class SnakeGame(object):

    def __init__(self, width, height, food):
        self.food = collections.deque(food)
        self.width = width
        self.height = height
        self.currH = 0
        self.currW = 0
        self.score = 0
        self.grid = collections.deque([(0,0)])
        self.direction = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1)}

    def move(self, direction):
        dx,dy = self.direction[direction]
        self.currH += dx
        self.currW += dy

        if self.food and [self.currH,self.currW] == self.food[0]:
            self.score += 1
            self.food.popleft()

        else:
            self.grid.popleft()

        if not 0<=self.currH<self.height or not 0<=self.currW<self.width or (self.currH,self.currW) in self.grid:
            return -1
        self.grid.append((self.currH,self.currW))
        
        return self.score




# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
