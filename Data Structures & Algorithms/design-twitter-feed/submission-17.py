class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time -= 1 # most recent will be smaller time -> heapify will put it at the top. 
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId)
        # now we need a frontier pointer for each followees list of tweets.
        # add them all to minHeap first and then pop off the top 10
        minHeap = [] 

        # 1. add each "frontier" (newest followee tweet) to the minHeap
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                numTweets = len(self.tweetMap[followeeId])
                tweetTime, tweetId = self.tweetMap[followeeId][-1]
                # 1. time (so heap orders by most recent tweet)
                # 2. tweetId (for adding to result)
                # 3. followeeId (so we know what map we're talking about when we need to go add the next one on the frontier)
                # 4. numTweets - 1is the return address, i.e. the index of the tweet we just pushed so we know where the frontier should get moved to.
                heapq.heappush(minHeap, (tweetTime, tweetId, followeeId, numTweets - 1))

        # 2. add the head of minHeap to the result
        # 3. and push the next tweet by that followee (frontier for that followee) onto the heap
        res = [] 
        while len(res) < 10 and minHeap:
            time, tweetId, authorId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            # 3. 
            index -= 1
            if index >= 0:
                time, tweetId = self.tweetMap[authorId][index]
                heapq.heappush(minHeap, (time, tweetId, authorId, index))
        
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId) # follower follows followee
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId) # follower unfollows followee
        
