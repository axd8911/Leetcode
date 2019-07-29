'''
Main approach: if a small number appears in left of a large number, this small number is a negative role
In main run time range. 60%

'''



class Solution:
    def romanToInt(self, s: str) -> int:
        dict_roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        if len(s) == 1:
            return dict_roman[s[0]]
        
        if len(s)>1:
            number = 0
            for i in range(len(s)-1):
                if dict_roman[s[i]] < dict_roman[s[i+1]]:
                    number -= dict_roman[s[i]]
                else:
                    number += dict_roman[s[i]]
                    
            return number + dict_roman[s[-1]]
            

        
