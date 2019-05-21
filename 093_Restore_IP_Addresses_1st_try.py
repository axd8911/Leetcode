'''
98.6%

backtracking: more practice makes better understanding
'''

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        output = []
        
        def bt(full, combine, rest, i):
            
            if combine and len(combine[-1]) == 0:
                return
            if combine and int(combine[-1]) > 255:
                return
            if combine and str(int(combine[-1])) != combine[-1]:
                return
            
            if rest > 3*(4-len(combine)) or rest < (4-len(combine)):
                return
            if rest == 0:
                output.append(combine)
                return
            
            bt(full[i:],combine + [s[i:i+1]],rest-1,i+1) or bt(full[i:],combine + [s[i:i+2]],rest-2,i+2) or bt(full[i:],combine + [s[i:i+3]],rest-3,i+3)
            
        if s:
            bt(s,[],len(s),0)
        
        output2 = []
        for item in output:
            output2.append(item[0]+'.'+item[1]+'.'+item[2]+'.'+item[3])
        
        return output2
