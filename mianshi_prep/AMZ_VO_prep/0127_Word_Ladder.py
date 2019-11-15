class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        length = len(beginWord)
        wordSet = collections.defaultdict(list)
        if endWord == beginWord:
            return 1
        for item in wordList:
            for i in range(length):
                wordSet[item[:i]+'*'+item[i+1:]].append(item)

        curr = collections.deque([beginWord])
        visited = set()
        step = 1
        while curr:
            step += 1
            l = len(curr)
            for i in range(l):
                item = curr.popleft()
                for i in range(length):
                    for word in wordSet[item[:i]+'*'+item[i+1:]]:
                        if word == endWord:
                            return step
                        if word not in visited:
                            visited.add(word)
                            curr.append(word)
        return 0
