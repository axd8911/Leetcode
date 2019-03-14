'''
A few hours of working made up of this approach.

Leetcode score: 88%. There is another main range faster than me.
Run time level: (n)

Comments:
Make good use of 0.5 in the situation of odd + even conditions.
Should be good if I can repeat my own process rapidly.

Another old slow approach is also here. Slow but clear short code, for loop in for loop. See bottom.

'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        long_loc = 0
        mover = 0
        
        if len(s)<=1:
            longest_string = s
            
        else:
            longest_string = ''
        
        a = [i/2 for i in range(0,2*(len(s)-1))]
        
        for i in a:
            if i>0 and i != int(i):
                mover = mover - 1    
                long_loc = long_loc - 1

            while mover>=long_loc and mover <= min(i,len(s)-1-i):

                if s[int(i):int(i)-mover:-1] + (s[int(i)-mover]) == s[int(round(i+0.4)):int(round(i+0.4))+mover] + s[int(round(i+0.4))+mover]:
                    
                    long_string = s[int(i)-mover:int(round(i+0.4))+mover+1]
                    mover = mover + 1
                else: break
            
            if len(long_string) > len(longest_string):
                longest_string = long_string
        
        
        return longest_string
        
        
        
 '''
 class Solution:
    def longestPalindrome(self, s: str) -> str:

        #s = list(s)
        longest = 1
        stop = 0
        longstring = s
        
        for i in range(len(s)-1,-1,-1):
            for j in range(0,len(s)-i):
                                
                if s[j:j+int(i/2)+1] == s[i+j:j+int(round(i/2+0.4))-1:-1]:
                    longest = i
                    longstring = s[j:i+j+1]
                    stop = 1
                    break
            if stop == 1:
                break

        return longstring
        
 '''
        
