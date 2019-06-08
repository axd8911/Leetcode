class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
    
        start = str(bin(n))[2:]
        addup = 32-len(start)
        end = '0'*addup + start 
        
        new = 0
        for i in range(len(end)):
            if end[i] == "1":
                new += 2**i

        
        
        return new
        
        
        
