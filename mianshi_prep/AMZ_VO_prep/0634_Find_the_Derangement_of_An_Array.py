class Solution:
    def findDerangement(self, n: int) -> int:

        # first num in other position, (n-1) conditions
        # second num in first position, making others to d(n-2) case
        # second num not in first position, making others to d(n-1) case

        twoBelow = 0
        oneBelow = 1

        if n == 1:
            return twoBelow
        if n == 2:
            return oneBelow

        for i in range(3,n+1):
            curr = (i-1)*(oneBelow + twoBelow)%(10**9+7)
            twoBelow = oneBelow
            oneBelow = curr

        return curr
