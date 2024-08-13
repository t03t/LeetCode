from collections import deque

class Twitter:
    class User:
        def __init__(self, userId: int):
            self.userId = userId
            self.tweets = deque()  # Using deque for fast appends and pops
            self.following = set()

        def follow(self, followeeId: int):
            if followeeId != self.userId:
                self.following.add(followeeId)

        def unfollow(self, followeeId: int):
            if followeeId in self.following:
                self.following.remove(followeeId)

        def post(self, tweetId: int, timestamp: int):
            self.tweets.appendleft((timestamp, tweetId))
            if len(self.tweets) > 10:
                self.tweets.pop()

        def getTweets(self):
            return list(self.tweets)

    def __init__(self):
        self.users = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = self.User(userId)
        self.users[userId].post(tweetId, self.timestamp)
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []

        # Gather the user's tweets and the tweets of followed users
        news_feed = list(self.users[userId].getTweets())
        for followeeId in self.users[userId].following:
            if followeeId in self.users:
                news_feed.extend(self.users[followeeId].getTweets())

        # Sort only if necessary, we limit the size to the 10 most recent tweets
        news_feed.sort(reverse=True, key=lambda x: x[0])
        return [tweetId for _, tweetId in news_feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = self.User(followerId)
        if followeeId not in self.users:
            self.users[followeeId] = self.User(followeeId)
        self.users[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users and followeeId in self.users:
            self.users[followerId].unfollow(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
