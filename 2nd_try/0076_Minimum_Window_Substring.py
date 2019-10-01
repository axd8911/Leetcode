class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_set = collections.defaultdict(int)
        for item in t:
            t_set[item]+=1

        left,right = 0,0
        length = len(t)
        window = ''
        for right in range(len(s)):
            if t_set[s[right]]>0:
                length -=1
            t_set[s[right]]-=1
            while length ==0:
                if not window or right+1-left<len(window):
                    window = s[left:right+1]
                t_set[s[left]]+=1
                if t_set[s[left]]>0:
                    length += 1
                left+=1
        return window
