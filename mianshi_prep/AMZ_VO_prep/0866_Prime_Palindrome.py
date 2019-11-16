class Solution:
    def primePalindrome(self, N: int) -> int:
        def isPrime(num):
            if num<=1:
                return False
            for i in range(2,int(num**0.5)+1):
                if num%i==0:
                    return False
            return True

        for i in range(1,6):
            for n in range(10**(i-1),10**i):
                s = str(n)
                combine = int(s + s[-2::-1])
                if combine >= N and isPrime(combine):
                    return combine
            for n in range(10**(i-1),10**i):
                s = str(n)
                combine = int(s + s[::-1])
                if combine >= N and isPrime(combine):
                    return combine

                
