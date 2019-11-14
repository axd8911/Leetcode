class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        d = set(words)
        def dfs(word):
            for i in range(1,len(word)):

                if word[:i] in d and (word[i:] in d or dfs(word[i:])):
                    return True

        res = []
        for item in words:
            if dfs(item):
                res.append(item)

        return res
