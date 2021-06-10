class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = collections.Counter(t)
        count_move = collections.defaultdict(int)
        total_amount = len(t)
        match = 0
        front,end = 0,0
        length = inf
        output = ''
        
        while front < len(s):
            if s[front] in count_t:
                if count_move[s[front]]<count_t[s[front]]:
                    match += 1
                count_move[s[front]] += 1
                while match==total_amount and end<=front:
                    if front-end+1<length:
                        length = front-end+1
                        output = s[end:front+1]
                    count_move[s[end]]-=1
                    if s[end] in count_t and count_move[s[end]]<count_t[s[end]]:
                        match -= 1
                        end+=1
                        break
                    end+=1
            front +=1
        return output
                    
            
