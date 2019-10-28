class Trie:
    def __init__(self):
        self.root = {}
    def add(self,word):
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.append('')
        myWords = set(words)
        myTrie = Trie()
        for item in words:
            myTrie.add(item)

        self.longest = 0
        self.res = []

        def helper(curr,combine):

            if combine in myWords:
                if len(combine)>self.longest:
                    self.res = [combine]
                    self.longest = len(combine)
                elif len(combine) == self.longest:
                    self.res.append(combine)

                for item in curr:
                    helper(curr[item],combine + item)

        helper(myTrie.root,'')

        return sorted(self.res)[0] if self.res else ''
