class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        if words == []:
            return []
        
        total_length = len(words) * len(words[0])
        
        word_dict = {}
        for word in words:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] = word_dict[word] + 1
        output = []
        temp_dict = {}
        for i in range(len(s)-total_length+1):
            
            if s[i:i+len(words[0])] in word_dict:
                temp_dict[s[i:i+len(words[0])]] = 1
                strings = 1
                while strings < len(words):
                    a = s[i+strings*len(words[0]):i+strings*len(words[0])+len(words[0])]
                    if a not in word_dict:
                        break
                    if a in temp_dict and temp_dict[a] == word_dict[a]:
                        break
                    if a in temp_dict:
                        temp_dict[a] = temp_dict[a] + 1
                    else:
                        temp_dict[a] = 1

                    strings = strings + 1
                if temp_dict == word_dict:
                    output.append(i)
                temp_dict = {}   
                    
            
                    
        return output
                        
                
                
