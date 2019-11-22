class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:

        dic = collections.defaultdict(int)
        dic[0]=1
        for i in range(d):
            newDic = collections.defaultdict(int)
            for curr in range(1,f+1):
                for key in dic:
                    newDic[curr+key] += dic[key]
            dic = newDic

        return dic[target]%(10**9+7)
        
