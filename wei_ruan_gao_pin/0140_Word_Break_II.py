class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # check which index can be true. When it is true, save the words combines in that index
        wordDict = set(wordDict)
        dic = collections.defaultdict(list)
        dic[0].append([])
        
        check = [True] + [False]*len(s)
        
        for i in range(len(s)):
            if check[i]:
                for j in range(i,len(s)+1):
                    if s[i:j] in wordDict:
                        check[j]=True
                        for item in dic[i]:
                            dic[j].append(item+[s[i:j]])

        return [' '.join(item) for item in dic[len(s)]]
