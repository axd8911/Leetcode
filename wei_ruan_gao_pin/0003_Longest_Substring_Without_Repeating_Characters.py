class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #做一个dict，里面保存的是每个字母的当前index
        #如果当前字母存在于字典，并且序列大于front，那就需要把front更新成那个序列的下一个，并且把需要更新成当前index
        front = 0
        maxLength = 0
        res = ''
        dict = collections.defaultdict(int)
        for i in range(len(s)):
            if s[i] in dict and dict[s[i]] >= front:
                front = dict[s[i]]+1
            dict[s[i]] = i
            if i-front+1>maxLength:
                res = s[front:i+1]
                maxLength = i-front+1
        return maxLength
                
