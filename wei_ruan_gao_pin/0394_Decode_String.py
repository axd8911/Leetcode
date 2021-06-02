class Solution:
    def reorganizeString(self, s: str) -> str:
        count = collections.Counter(s)
        maximum = max(count.values())
        length = len(s)
        if maximum>math.ceil(length/2):
            return ''
        
        heap = [(-count[item],item) for item in count]
        heapq.heapify(heap)
        output = ''
        while heap:
            top_count, top_letter = heapq.heappop(heap)
            if output == '' or output[-1]!=top_letter:
                top_count += 1
                output += top_letter
            else:
                sec_count,sec_letter = heapq.heappop(heap)
                output += sec_letter
                sec_count += 1
                if sec_count != 0:
                    heapq.heappush(heap,(sec_count,sec_letter))
            if top_count != 0:
                heapq.heappush(heap,(top_count,top_letter))
        return output
