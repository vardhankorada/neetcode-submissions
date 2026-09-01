class Solution:
    def topKFrequent(self, nums: List[int], want: int) -> List[int]:
        store,ans = {},[]
        for num in nums: store[num] = store.get(num,0)+1
        freq = [[] for i in range(1,len(nums)+1)]
        for k,v in store.items():freq[v-1].append(k)
        for i in range(len(freq)-1,-1,-1):
            for ele in freq[i]: ans.append(ele)
            if len(ans) == want: return ans