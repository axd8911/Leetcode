'''
90%
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        head = 0
        foot = len(s)-1
        valid = {item:None for item in 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM'}
        while head < foot:
            if s[head] not in valid:
                head = head + 1
                continue
            if s[foot] not in valid:
                foot = foot - 1
                continue
                
            if s[head].upper() == s[foot].upper():
                head = head + 1
                foot = foot - 1
                continue
            else:
                return False
            
        return True
