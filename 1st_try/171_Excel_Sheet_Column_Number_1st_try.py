'''
90%
'''

class Solution:
    def titleToNumber(self, s: str) -> int:
        
        letters = [chr(item) for item in range(ord('A'),ord('Z')+1)]
        numbers = [item for item in range(1,27)]
        
        match = {letter:number for letter,number in zip(letters,numbers)}

        result = 0
 
        for i in range(len(s)):
 
            result = result + match[s[i]]*(26**(len(s)-1-i))
            
        return result
