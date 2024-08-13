import heapq

class Twitter:
    class User:
        def __init__(self, userId: int):
            self.userId = userId
            self.tweets = []
            self.following = set()

        def follow(self, followeeId: int):
            if followeeId != self.userId:
                self.following.add(followeeId)

        def unfollow(self, followeeId: int):
            if followeeId in self.following:
                self.following.remove(followeeId)

        def post(self, tweetId: int, timestamp: int):
            self.tweets.append((timestamp, tweetId))

        def getNewsFeed(self, allUsers):
            min_heap = []
            for tweet in self.tweets:
                if len(min_heap) < 10:
                    heapq.heappush(min_heap, tweet)
                else:
                    heapq.heappushpop(min_heap, tweet)
                    
            for followeeId in self.following:
                if followeeId in allUsers:
                    for tweet in allUsers[followeeId].tweets:
                        if len(min_heap) < 10:
                            heapq.heappush(min_heap, tweet)
                        else:
                            heapq.heappushpop(min_heap, tweet)

            # We now have the 10 most recent tweets in the heap, but they may not be in order.
            # We need to pop all items from the heap to get them in order from most recent to oldest.
            return [tweetId for _, tweetId in sorted(min_heap, reverse=True)]


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

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users and followeeId in self.users:
            self.users[followerId].unfollow(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
