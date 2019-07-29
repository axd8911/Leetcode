'''
57%, between the two major runtime peaks.
There is another apporach which is three times faster, using defaultdict from collections. It is useful to learn about that.
BFS

'''


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        search = {}
        search[beginWord] = None
        search_next = {}
        count = 0
        
        while search != {}:
            if endWord in search:
                return count+1
            subsearch = []
            for i in range(len(beginWord)):
                subsearch = {}
                for key in search.keys():
                    subsearch[key[:i] + key[i+1:]] = None
                    
                n = 0
                while n < len(wordList):
                    if wordList[n][:i] + wordList[n][i+1:] in subsearch:
                        search_next[wordList.pop(n)] = None
                    else:
                        n = n + 1
                      
            search = search_next
            search_next = {}
            count = count + 1
        return 0
    
