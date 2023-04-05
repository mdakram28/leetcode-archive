from queue import Queue
class Twitter:

    def __init__(self):
        self.following = collections.defaultdict(set)
        self.tweets = collections.defaultdict(list)
        self.time = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.following[userId].add(userId)
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        tweets = [self.tweets[f] for f in self.following[userId]]
        idx = [len(t)-1 for t in tweets]
        max_tweets = min(sum(len(t) for t in tweets), 10)
        while len(feed) < max_tweets:
            latest = max((t[idx[ui]], ui) for ui, t in enumerate(tweets) if idx[ui] >= 0 )
            idx[latest[1]] -= 1
            feed.append(latest[0][1])

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)