class Solution:
    def countingBits(self,n):
        digits = []
        res = n
        while res != 0:
            digits.append(res%2)
            res //= 2
        digits.append(0)
        digits = digits[::-1]

        output = []
        total = 0
        for i in range(len(digits)):
            if digits[i]==1:
                output.append(i)
                total+=1
        return [total]+output

def main():
    n = 5
    print (Solution().countingBits(n))
main()
