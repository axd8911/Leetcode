'''
71%
'''

#Solution 1
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = 0
        for item in reversed(s):
            if item != ' ':
                n = n + 1
            if n != 0 and item == ' ':
                break
        return n
        
#Solution 2
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split(' ')
        s = [item for item in s if item != '']
        
        if s == []:
            return 0
        return len(s[-1])
