class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        if not l1 or not l2:
            return l1 or l2
        memo = [[None for _ in range(l2)] for _ in range(l1)]
        def helper(i,j):
            if i == l1:
                return l2-j
            if j == l2:
                return l1-i
            if memo[i][j]:
                return memo[i][j]
            if word1[i]==word2[j]:
                ans = helper(i+1,j+1)
            else:
                ans = min(helper(i+1,j),helper(i,j+1),helper(i+1,j+1))+1
            memo[i][j] = ans
            return memo[i][j]

        helper(0,0)
        print (memo)
        return memo[0][0]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1,l2 = len(word1),len(word2)


        memo = [[None for _ in range(l2+1)]  for _ in range(l1+1)]

        for i in range(l1+1):
            memo[i][l2] = l1-i
        for j in range(l2+1):
            memo[l1][j] = l2-j

        for i in range(l1-1,-1,-1):
            for j in range(l2-1,-1,-1):
                if word1[i] == word2[j]:
                    memo[i][j] = memo[i+1][j+1]
                else:
                    memo[i][j] = min(memo[i+1][j],memo[i][j+1],memo[i+1][j+1])+1
        #print (memo)
        return memo[0][0]
