class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # from 1 to sqrt
        count = 0
        for i in range(1, n+1):
            curr = n/i
            if curr - i/2<0:
                break
            if i%2 == 0:
                if curr != int(curr) and curr * 2 == int (curr*2):
                    count += 1
            else:
                if curr == int(curr):
                    count += 1
        return count
