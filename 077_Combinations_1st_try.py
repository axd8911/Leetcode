'''
30%
very slow. should learn the faster approaches
'''


#recursion
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        setN = [item for item in range(1,n+1)]
        
        output = []
        
        def bt(allData,combine,k):
            if len(combine) == k:
                output.append(combine)
                return
                
            for i in range(len(allData)):
                bt(allData[i+1:],combine+[allData[i]],k)
                
                
        if setN:
            bt(setN, [], k)
            
        return output
        
        
 #iteration
 class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        combine = [[item] for item in range(1,n+1)]
        
        for i in range(k-1):
            new = []
            for item in combine:
                for m in range(item[-1]+1, n+1):
                    new.append(item+[m])
                    
            combine = new
            
            
        return combine
