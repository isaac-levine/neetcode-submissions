class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list) # user -> [(time, tweetId), (...), ...]
        self.followMap = defaultdict(set) # user -> set of followees
        self.count = 0 # decreasing timestamp for ordering tweets
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    
    def getNewsFeed(self, userId: int) -> List[int]:
        # get the 10 most recent tweetIds in the userId's news feed. (ordered from most recent to least)
        res = [] 
        minHeap = []

        self.followMap[userId].add(userId) # make the user follow itself

        # add the frontier of each followee to the minHeap
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                # get the tweets for this followee
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [time, tweetId, followeeId, index - 1]) # why - 1 here?

        while len(res) < 10 and minHeap: 
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        return res
        
    
    # followerId followers followeeId
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap and followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
        
