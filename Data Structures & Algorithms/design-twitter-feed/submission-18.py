class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set) # userId -> (follows) -> Set(user1, user2)
        self.tweetMap = defaultdict(list) # [(time, tweetId), ...]
        self.time = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time -= 1 # we go negative because we want the newest time to be popped off the minHeap first.

    def getNewsFeed(self, userId: int) -> List[int]:
        # off bat I remember that we want the heap entries to tell us everything
        # we need to locate the frontier for that author 
        # result = most recent to least recent tweetIds
        res = [] 
        minHeap = []  # (time, tweetId, authorId, indexOfTweetId)
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            # queue up each person's most recent tweet into the minHeap
            if followeeId in self.tweetMap:
                tweetsByFolloweeId = self.tweetMap[followeeId]
                i = len(tweetsByFolloweeId) - 1
                time, tweetId = tweetsByFolloweeId[i]
                heapq.heappush(minHeap, (time, tweetId, followeeId, i)) # push index of this tweetId
        
        while minHeap and len(res) < 10:
            time, tweetId, authorId, i = heapq.heappop(minHeap)
            res.append(tweetId)

            # add the next frontier tweet from this author to the minHeap if there are more tweets left.
            if i > 0:
                time, tweetId = self.tweetMap[authorId][i - 1] # just overriding the above variables since we don't need those anymore 
                heapq.heappush(minHeap, (time, tweetId, authorId, i - 1))
        
        return res


        

    def follow(self, followerId: int, followeeId: int) -> None:
        # followerId follows followeeId
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            # followerId unfollows followeeId
            self.followMap[followerId].remove(followeeId)
        
