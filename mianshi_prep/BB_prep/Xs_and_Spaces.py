class Solution:
    def xAndSpace(self,n):
        output = [[' ' for _ in range(n)] for _ in range(n)]
        for i in range(n):
            output[i][i], output[i][n-i-1] = 'x','x'
        return output

def main():
    n = 1
    result = Solution().xAndSpace(n)
    for i in range(n):
        print (''.join(result[i]))
main()
