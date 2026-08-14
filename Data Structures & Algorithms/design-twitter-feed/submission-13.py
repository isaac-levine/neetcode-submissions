class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set) # followMap[userId] -> set of users they follow 
        self.tweetMap = defaultdict(list) # tweetMap[userId] = all of userId's tweets (time, tweetId)
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1 # newer tweets have smaller values 
        self.tweetMap[userId].append((self.time, tweetId))
        # optimization: we will never need the 11th oldest tweet for any user
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)
        
    # get the 10 most refent tweets posted by all users that userId follows (including userId)
    # "top k" -> minHeap or quickSelect 
    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId) # make the user follow himself
        minHeap = [] # (time, tweetId, indexInAuthorsTweets)
        
        # add each "frontier" (newest followee tweet) to the minHeap
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                numTweets = len(self.tweetMap[followeeId])
                tweetTime, tweetId = self.tweetMap[followeeId][numTweets - 1]
                heapq.heappush(minHeap, ((tweetTime, tweetId, followeeId, numTweets - 1)))
        
        # add head of minHeap to res, and push next tweet by that followee (using index)
        res = []
        while len(res) < 10 and minHeap:
            time, tweetId, authorId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            index -= 1
            if index >= 0:
                tweetsByAuthor = self.tweetMap[authorId]
                nextTime, nextTweetId = tweetsByAuthor[index] 
                heapq.heappush(minHeap, (nextTime, nextTweetId, authorId, index))
            
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
