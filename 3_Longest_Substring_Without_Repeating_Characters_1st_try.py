'''
Leetcode score: 90%
Memory usage: 5% - What's wrong? Should get some time and solve this issue. always there.

Please, pay enough attention on the boundary details.
For example: temp_long = len(substring) - obviously it should be counted before deleting anything
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        substring = []
        longest = 0
        
        for item in s:
            if item not in substring:
                substring.append(item)
            else:
                temp_long = len(substring)
                del substring[0:substring.index(item)+1]
                substring.append(item)
                
                if temp_long > longest:
                    longest = temp_long
                    
        if len(substring) > longest:
            longest = len(substring)
                          
        return longest
