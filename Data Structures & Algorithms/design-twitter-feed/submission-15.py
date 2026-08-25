class Twitter:

    def __init__(self):
        # userId -> Set<(userId)
        self.followMap = defaultdict(set) # need to support O(1) add and remove  

        # userId -> List<(time, tweetId)> -- should be able to pop from the back like a stack
        self.tweetMap = defaultdict(list) # need to be able to iterate with pointers in getNewsFeed
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        self.tweetMap[userId].append((self.time, tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId)
        # naive solution: get all the tweets of everyone they follow, then get top k newest.
        # better: maintain a frontier pointer on each followee's tweetMap...

        res = []  # the top k newest tweetIds 
        minHeap = []  # (time, tweetId, authorId, indexInAuthorsTweets) -- remember time is negative so we get the newest tweets first

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                frontierIndex = len(self.tweetMap[followeeId]) - 1
                tweetTime, tweetId = self.tweetMap[followeeId][frontierIndex]
                heapq.heappush(minHeap, (tweetTime, tweetId, followeeId, frontierIndex))

        res = [] 
        while len(res) < 10 and minHeap:
            
            # add the head of the heap to the res, and push the next frontier for that author
            _, tweetId, authorId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            
            index -= 1
            if index >= 0:
                time, tweetId = self.tweetMap[authorId][index]
                heapq.heappush(minHeap, (time, tweetId, authorId, index))

        return res
                        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
