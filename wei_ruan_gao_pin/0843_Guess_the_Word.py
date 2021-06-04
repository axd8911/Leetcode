# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def match(w1,w2):
            return sum(w1[i]==w2[i] for i in range(6))
        while wordlist:
            count = [collections.Counter(item[i] for item in wordlist) for i in range(6)]
            guess = max(wordlist,key=lambda x:sum(count[i][x[i]] for i in range(len(x))))
            number = master.guess(guess)
            wordlist = [item for item in wordlist if match(guess,item)==number]
            if number == 6:
                break
