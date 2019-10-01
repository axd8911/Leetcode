class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort based on small end
        #if output is empty, or curr small bigger than output large,add curr

        intervals.sort()
        output = []
        for item in intervals:
            if not output or output[-1][1]<item[0]:
                output.append(item)
            else:
                output[-1][1] = max(output[-1][1],item[1])
        return output
