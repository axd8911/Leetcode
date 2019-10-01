class Solution:
    def romanToInt(self, s: str) -> int:
        letter = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total = 0
        for i in range(len(s)-1):
            if letter[s[i]]<letter[s[i+1]]:
                total -= letter[s[i]]
            else:
                total += letter[s[i]]

        return total + letter[s[-1]]
