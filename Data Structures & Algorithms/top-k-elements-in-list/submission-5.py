class Solution:
    def topKFrequent(self, nums: List[int], t: int) -> List[int]:
        store = {}
        for num in nums: store[num] = store.get(num,0)+1
        return [k for k,v in sorted(store.items(),key= lambda x : x[1], reverse=True)][:t]