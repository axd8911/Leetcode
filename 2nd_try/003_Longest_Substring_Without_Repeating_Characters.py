class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #set a hashmap: save location of a letter
        #start point is zero. If a letter is repeating, update start point to max(start point, last letter position+1). Keep a record on longest

        position = {}
        start = 0
        longest = 0
        curr = 0

        for i in range(len(s)):
            if s[i] in position and position[s[i]]>=start:
                start = position[s[i]]
                longest = max(longest,curr)
                curr = i-start

            else:
                curr += 1
            position[s[i]] = i

        return max(curr,longest)
