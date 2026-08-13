class Twitter:

    def __init__(self):
        self.followers = defaultdict(set) # followers[userId] = everyone who follows userId
        self.following = defaultdict(set) # following[userId] = everyone userId is following 
        self.tweetMap = defaultdict(list) # tweetMap[userId] = all of userId's tweets (time, tweetId)
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1 # going down so that we can have a minHeap with most recent tweets
        self.tweetMap[userId].append((self.time, tweetId))
        

    # get the 10 most refent tweets posted by all users that userId follows (including userId)
    # "top k" -> minHeap or quickSelect 
    def getNewsFeed(self, userId: int) -> List[int]:
        # get the tweets of everyone this user follows (including userId)
        self.follow(userId, userId)
        minHeap = [] # all tweets posted by everyone userId follows
        for followee in self.following[userId]:
            for tweetTime, tweetId in self.tweetMap[followee]:
                minHeap.append((tweetTime, tweetId))
        heapq.heapify(minHeap)
        res = []
        for _ in range(10):
            if minHeap:
                res.append(heapq.heappop(minHeap)[1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId) # followerId following followeeId
        self.followers[followeeId].add(followerId) # followeeId followed by followerId
        
    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        # followerId no longer follows followeeId
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId) # followerId no longer following follweeId
        if followerId in self.followers[followeeId]:
            self.followers[followeeId].remove(followerId) # follower on longer a follower of followeeId
