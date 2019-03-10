'''
A easy one, but any simple and smart improvement can make the speed much faster
Leetcode score: 12%

Comments:
1. The smart solution inverse the string to work more efficiently
2. A few list operations: list.split(), 'some_symbol'.join(you_list) can make you list into string

A crazy solution
        S = S.replace('-','').upper()[::-1]
        print (S)
        
        return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]


'''

class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        
        S = S.replace('-','')
        S = S.upper()

        for i in range(len(S)-K,0,-K):
            S = S[0:i] + '-' + S[i:]
        return S
                
