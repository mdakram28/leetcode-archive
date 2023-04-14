class TweetCounts:

    def __init__(self):
        # self.tweets = collections.defaultdict(set)
        # self.freq = collections.defaultdict(lambda: collections.defaultdict(int))
        self.by_day = collections.defaultdict(
            lambda: collections.defaultdict(int)
        )
        self.by_hour = collections.defaultdict(
            lambda: collections.defaultdict(int)
        )
        self.by_min = collections.defaultdict(
            lambda: collections.defaultdict(int)
        )
        self.by_sec = collections.defaultdict(
            lambda: collections.defaultdict(int)
        )

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.by_sec[tweetName][time] += 1
        time //= 60
        self.by_min[tweetName][time] += 1
        time //= 60
        self.by_hour[tweetName][time] += 1
        time //= 24
        self.by_day[tweetName][time] += 1

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        steps = 60
        if freq == "hour":
            steps = 3600
        elif freq == "day":
            steps = 86400
        by_day = self.by_day[tweetName]
        by_hour = self.by_hour[tweetName]
        by_min = self.by_min[tweetName]
        by_sec = self.by_sec[tweetName]

        def get_upto_exc(start, end):
            day = start//86400, end//86400
            hour = start//3600, end//3600
            minute = start//60, end//60
            # print(
            #     (start, end), day, hour, minute,
            #     sum(by_day[i] for i in range(day[0], day[1]))
            #     ,sum(by_hour[i] for i in range(day[0]*24, hour[0]))
            #     ,sum(by_min[i] for i in range(hour[0]*60, minute[0]))
            #     ,sum(by_sec[i] for i in range(minute[0]*60, start))
            #     ,sum(by_hour[i] for i in range(day[1]*24, hour[1]))
            #     ,sum(by_min[i] for i in range(hour[1]*60, minute[1]))
            #     ,sum(by_sec[i] for i in range(minute[1]*60, end))
            # )
            return (
                  sum(by_day[i] for i in range(day[0], day[1]))
                - sum(by_hour[i] for i in range(day[0]*24, hour[0]))
                - sum(by_min[i] for i in range(hour[0]*60, minute[0]))
                - sum(by_sec[i] for i in range(minute[0]*60, start))
                + sum(by_hour[i] for i in range(day[1]*24, hour[1]))
                + sum(by_min[i] for i in range(hour[1]*60, minute[1]))
                + sum(by_sec[i] for i in range(minute[1]*60, end))
            )

        # if len(ret) == 24 and all(v==0 for v in ret):
        #     print("Found", freq, tweetName, startTime, endTime)
        return [
            get_upto_exc(startTime+i*steps, min(startTime+(i+1)*steps, endTime+1))
            for i in range((endTime-startTime)//steps + 1)
        ]


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)