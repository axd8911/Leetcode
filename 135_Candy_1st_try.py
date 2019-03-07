'''
Leetcode run time score: 56%, in the main range
Run time level: (n) - linear

Comments:
1. (Obviously) One for loop is much faster than for loop in for loop
2. Boundary situations of this problem is quite complicated. A few hours of thinking and clarifying is worthy.
3. Pay attention to the 'if' 'else' logics. If two ifs overlap each other, you may do something repeatedly. Jump out in time!
    (line 41 and 45)
'''

class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        start = 0
        sub_ratings = []
        total = 0
        if len(ratings) == 1:
            return 1
        
        if ratings[0] == ratings[1]:
            sub_ratings.append(ratings[0:1])

        for i in range(1,len(ratings)-1):
            if ratings[i] <= ratings[i-1] and ratings[i] <= ratings[i+1]:
                sub_ratings.append(ratings[start:i+1])
                start = i
                
        sub_ratings.append(ratings[start:])
        
        for item in sub_ratings:
            peak = item.index(max(item))
            long_distance = max(peak - 0, len(item)-1-peak)            
            
            if len(item) == 2 and item[0] == item[1]:
                sub_total = 2
                total = total + sub_total
                continue
            if peak<len(item)-2 and item[peak] == item[peak+1]:
                sub_total = sum(range(long_distance+1)) + sum(range(len(item)-long_distance+1))
                total = total + sub_total
                continue
            
            else:
                sub_total = sum(range(long_distance+2)) + sum(range(len(item)-long_distance))
                total = total + sub_total

        total = total - len(sub_ratings) + 1
        
        return (total)
