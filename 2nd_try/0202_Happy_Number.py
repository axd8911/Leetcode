class Solution:
    def isHappy(self, n: int) -> bool:
        curr = n
        new = 0
        exist = set()

        while curr not in exist:
            #print (exist)
            exist.add(curr)
            new = 0
            while curr != 0:
                rem = curr%10
                curr//=10
                new += rem**2
                #print (new,rem,curr)
            curr = new

        if curr == 1:
            return True
        return False
