class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderDict = collections.defaultdict(int)
        for i in range(len(order)):
            orderDict[order[i]] = i
        res = []
        for word in words:
            res.append([])
            for letter in word:
                res[-1].append(orderDict[letter])
        for i in range(1,len(res)):
            if res[i]<res[i-1]:
                return False
        return True
