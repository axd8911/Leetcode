class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # create a huge dict: save all words with each letter replaced by '*'
        star = collections.defaultdict(set)
        for w in wordList:
            for i in range(len(w)):
                star[w[:i]+'*'+w[i+1:]].add(w)
        output = 1
        curr = set()
        curr.add(beginWord)
        visited = set()

        while curr:
            output += 1
            new = set()
            for w in curr:
                for i in range(len(w)):
                    comb =w[:i] + '*' + w[i+1:]
                    if endWord in star[comb]:
                        return output
                    for item in star[comb]:
                        if item not in visited:
                            new.add(item)
                            visited.add(item)

            curr = new
            #print (curr,visited)

        return 0


        
