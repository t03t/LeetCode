
class Twitter:
    class User:
        def __init__(self, userId: int, tweets=None, followers=None, following=None):
            self.userId = userId
            self.tweets = tweets if tweets is not None else []
            self.followers = followers if followers is not None else []
            self.following = following if following is not None else []

        def follow(self, followerId: int):
            if followerId not in self.following:
                self.following.append(followerId)

        def unfollow(self, followerId: int):
            if followerId in self.following:
                self.following.remove(followerId)

        def getFollowedBy(self, followerId: int):
            self.followers.append(followerId)

        def getUnfollowedBy(self, followerId: int):
            if followerId in self.followers:
                self.followers.remove(followerId)

        def post(self, tweetId: int, timestamp: int):
            self.tweets.append((timestamp, tweetId))

        def getTweets(self):
            return self.tweets

        def getNewsFeed(self, allUsers):
            allNews = []
            # Include the user's own tweets
            allNews.extend(self.tweets)
            # Include the tweets from users this user is following
            seen_tweets = set()
            for userId in self.following:
                if userId in allUsers:
                    for tweet in allUsers[userId].tweets:
                        if tweet[1] not in seen_tweets:
                            seen_tweets.add(tweet[1])
                            allNews.append(tweet)
            # Sort by timestamp in reverse order
            allNews.sort(reverse=True, key=lambda x: x[0])
            return [tweetId for _, tweetId in allNews[:10]]


    def __init__(self):
        self.users = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = self.User(userId)
        self.users[userId].post(tweetId, self.timestamp)
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId in self.users:
            return self.users[userId].getNewsFeed(self.users)
        return []

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = self.User(followerId)
        if followeeId not in self.users:
            self.users[followeeId] = self.User(followeeId)
        self.users[followerId].follow(followeeId)
        self.users[followeeId].getFollowedBy(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users and followeeId in self.users:
            self.users[followerId].unfollow(followeeId)
            self.users[followeeId].getUnfollowedBy(followerId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)