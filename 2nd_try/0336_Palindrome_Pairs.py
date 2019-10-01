class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        output = set()
        rev = {s[::-1]:i for i,s in enumerate(words)}
        for i,s in enumerate(words):
            for j in range(len(s)+1):
                l,r = s[:j],s[j:]
                if l in rev and i != rev[l] and r==r[::-1]:
                    output.add((i,rev[l]))
                if r in rev and i != rev[r] and l==l[::-1]:
                    output.add((rev[r],i))
        return output
        
