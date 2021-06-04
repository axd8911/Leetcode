class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        output = 0
        for i in range(len(s)):
            if i==len(s)-1 or mapping[s[i]]>=mapping[s[i+1]]:
                output += mapping[s[i]]
            else:
                output-=mapping[s[i]]
        return output
