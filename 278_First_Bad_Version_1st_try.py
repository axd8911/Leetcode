'''
75%
Should practise more about 二分查找 and other basic algorithms like this.
'''


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        pos = n / 2
        mover = n / 2
        
        while True:
            mover = mover / 2
            if isBadVersion(round(pos)) == True:
                pos = pos - mover
            else:
                pos = pos + mover
            if mover <0.5:
                return round(pos+0.5)
        
        
