# place all buildings
# convert 1D locations to 2D locations
# remove duplicated combinations
import collections
import time
def solutions(h,w,n):
    size = h*w
    locs = [item for item in range(size)]
    combines = []

    def locations(combine, rest, idx):
        if len(combine) == n:
            combines.append(combine)
            return
        for i in range(idx,len(rest)):
            locations(combine +[rest[i]],rest[:i]+rest[i+1:],i)

    locations([],locs,0)

    def convert(num):
        y = (num+1)%w -1
        x = (num)//w
        if y==-1:y+=w
        return (x,y)

    for i in range(len(combines)):
        for j in range(len(combines[i])):
            combines[i][j] = convert(combines[i][j])
    print (len(combines))
    existing = set()
    for combine in combines:
        r1,r2,r3 = [],[],[]
        for x,y in combine:
            r1.append((h-x-1,y))
            r2.append((x,w-y-1))
            r3.append((h-x-1,w-y-1))
        #print (tuple(r1))
        r1.sort()
        r2.sort()
        r3.sort()
        if tuple(r1) not in existing and tuple(r2) not in existing and tuple(r3) not in existing:
            existing.add(tuple(combine))
    combines = list(existing)
    print (len(combines))

    shortest = float('inf')
    def bfs(combine):
        field = [[0 for i in range(w)] for j in range(h)]
        for x,y in combine:
            field[x][y] = 1
        visited = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        curr = collections.deque(combine)
        distance = 0
        while curr:
            length = len(curr)
            for i in range(length):
                x,y = curr.popleft()
                for dx,dy in directions:
                    if 0<=x+dx<h and 0<=y+dy<w and (x+dx,y+dy) not in visited and field[x+dx][y+dy] ==0:
                        curr.append((x+dx,y+dy))
                        visited.add((x+dx,y+dy))
            if curr:
                distance += 1
        return distance
    for combine in combines:
        a = bfs(combine)
        shortest = min(shortest,a)




    return shortest
A = time.time()
print (solutions(4,7,3))
B = time.time()
print (B-A)
