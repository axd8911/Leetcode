class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_log = []
        digit_log = []
        
        for log in logs:
            curr = log.split(' ')
            if curr[1].isdigit():
                digit_log.append(log)
            else:
                heapq.heappush(letter_log, [' '.join(curr[1:]),curr[0]])
        
        output = []
        while letter_log:
            curr = heapq.heappop(letter_log)
            output.append(curr[1]+' '+curr[0])
        output += digit_log
        return output
