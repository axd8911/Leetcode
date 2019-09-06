class Solution:
    def meetingRooms(self,intervals):
        # sort intervals
        # ------
        #    -----
        #     ---
        #        ---

        # ------
        #     ---
        #    -----
        #        ---
        intervals.sort(key=lambda x:x[1])
        time = []
        for interval in intervals:
            if time and interval[0]>=time[0]:
                time.pop(0)
            time.append(interval[1])
        return len(time)

def main():
    intervals = [[0, 30],[5, 10],[15, 20],[9,16],[7,12]]
    res = Solution().meetingRooms(intervals)
    print (res)

main()
