'''
78%

hash table question, use dictionary
each dict key is the sorted string
output the dictionary values
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = {}
        dict_strs = {item:''.join(sorted(item)) for item in strs}

        for item in strs:
            if dict_strs[item] in output:
                output[dict_strs[item]].append(item)
            else:
                output[dict_strs[item]] = [item]
            
        return list(output.values())
            
            

                
                
