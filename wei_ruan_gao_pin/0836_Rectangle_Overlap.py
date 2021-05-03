class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        def intersect(pl,ql,pr,qr):
            return min(pr,qr) > max(pl,ql)
        return intersect(rec1[0],rec2[0],rec1[2],rec2[2]) and intersect(rec1[1],rec2[1],rec1[3],rec2[3])
