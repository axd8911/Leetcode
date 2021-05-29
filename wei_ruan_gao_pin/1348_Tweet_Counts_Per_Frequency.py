class TweetCounts:

    def __init__(self):
        self.tweets = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        idx = bisect.bisect(self.tweets[tweetName],time)
        self.tweets[tweetName].insert(idx,time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        match = {'minute':60,'hour':3600,'day':86400}
        interval = match[freq]
        output = [0 for i in range((endTime-startTime)//interval+1)]
        l = bisect.bisect_left(self.tweets[tweetName],startTime)
        r = bisect.bisect_right(self.tweets[tweetName],endTime)
        time_range = self.tweets[tweetName][l:r]
        for time in time_range:
            output[(time-startTime)//interval] += 1
        return output
        

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
