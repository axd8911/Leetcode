class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        wordDict = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                wordDict[word[:i]+'?'+word[i+1:]].append(word)
        
        visited = set()
        curr = collections.deque([beginWord])
        step = 0
        while curr:
            step+=1
            if endWord in curr:
                return step
            length = len(curr)
            for i in range(length):
                add_word = curr.popleft()
                for j in range(len(add_word)):
                    rough_word = add_word[:j]+'?'+add_word[j+1:]
                    for word in wordDict[rough_word]:
                        if word not in visited:
                            curr.append(word)
                            visited.add(word)
        return 0
    #time O(M N^2)
    #space O(M N^2)
                        
