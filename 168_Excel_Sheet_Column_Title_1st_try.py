class Solution:
    def convertToTitle(self, n: int) -> str:
        letters = [chr(item) for item in range(ord('A'),ord('Z')+1)]
        numbers = [item for item in range(1,27)]
        
        match = {number:letter for number,letter in zip(numbers,letters)}
        match[0] = 'Z'
        digit = ''
        
        while n>0:
            digit += match[n%26]
            if n%26 == 0:
                n = n//26-1
            else:
                n = n//26
            
        return digit[::-1]
