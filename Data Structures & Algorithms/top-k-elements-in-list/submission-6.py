class Solution:
    # def topKFrequent(self, nums: List[int], t: int) -> List[int]:
    #     store = {}
    #     for num in nums: store[num] = store.get(num,0)+1
    #     return [k for k,v in sorted(store.items(),key= lambda x : x[1], reverse=True)][:t]


### Only K-from sorted ==> HeapMin
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res