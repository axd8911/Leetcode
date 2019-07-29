class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.allWords = set()
        self.start = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        length = len(word)
        self.allWords.add(word)
        
        for i in range(length+1):
            if i in self.start:
                self.start[i].add(word[:i])
            else:
                self.start[i] = set([word[:i]],)
            
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.allWords
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        #print (self.start)
        if len(prefix) in self.start:
            return prefix in self.start[len(prefix)]
        else:
            return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
