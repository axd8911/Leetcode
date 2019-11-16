class Trie:
    def __init__(self):
        self.dict = {}

    def add(self,word):
        curr = self.dict
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr['*'] = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for item in words:
            trie.add(item)
        res = set()
        h = len(board)
        w = len(board[0])
        visited = set()

        def dfs(currDict,i,j):
            char = board[i][j]
            currDict = currDict[char]

            if '*' in currDict:
                res.add(currDict["*"])

            visited.add((i,j))
            for dx,dy in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                if (dx,dy) not in visited and 0<=dx<h and 0<=dy<w and board[dx][dy] in currDict:
                    dfs(currDict,dx,dy)
            visited.remove((i,j))

        for i in range(h):
            for j in range(w):
                if board[i][j] in trie.dict:
                    dfs(trie.dict,i,j)

        return res
