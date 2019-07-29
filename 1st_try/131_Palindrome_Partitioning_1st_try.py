'''
90%


'''


class Solution:
        
    def partition(self, s: str) -> List[List[str]]:
        self.output = []
        
        def bt(string, combine):
            if string == '':
                self.output.append(combine[:])
            for i in range(1,len(string)+1):
                if string[:i] == string[:i][::-1]:
                    bt(string[i:],combine+[string[:i]])

        bt(s,[])
                
        return self.output
        
