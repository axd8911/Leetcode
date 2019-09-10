import collections
import heapq

class PathCalculator:
    def __init__(self):
        self.longest = 0
        self.l1 = None
        self.mid = None
        self.l2 = None
        self.connects = collections.defaultdict(list)

    def process(self,line):
        # dic: city: [(-distance,city)]
        a,b,distance = line.split(':')
        heapq.heappush(self.connects[a],(-int(distance),b))
        heapq.heappush(self.connects[b],(-int(distance),a))

        if len(self.connects[a])>=2:
            a1, a2 = heapq.nsmallest(2,self.connects[a])
            curr = -a1[0]-a2[0]
            if curr>self.longest or (curr==self.longest and (self.l1,self.mid,self.l2)>(a1[1],a,a2[1])):
                self.longest,self.l1,self.mid,self.l2 = curr,min(a1[1],a2[1]),a,max(a1[1],a2[1])

        if len(self.connects[b])>=2:
            b1, b2 = heapq.nsmallest(2,self.connects[b])
            curr = -b1[0]-b2[0]
            if curr>self.longest or (curr==self.longest and (self.l1,self.mid,self.l2)>(b1[1],b,b2[1])):
                self.longest,self.l1,self.mid,self.l2 = curr,min(b1[1],b2[1]),b,max(b1[1],b2[1])
        if not self.l1:
            return 'NONE'
        else:
            return str(self.longest) + ':' + self.l1 + ':' + self.mid + ':' + self.l2


if __name__ == "__main__":
    calc = PathCalculator()
    lines = ['CHI:NYC:719','NYC:LA:2414','NYC:SEATTLE:2448','NYC:HAWAII:4924','NYC:AWAII:4924']
    for line in lines:
        print (calc.process(line))
