class Solution:
    def rob(self, nums: List[int]) -> int:
        store = {}
        def rob_houses(ind):
            if ind >= len(nums): return 0
            if ind == len(nums)-1: return nums[-1]
            if ind == len(nums)-2: return max(nums[-1],nums[-2])
            if ind in store.keys(): return store[ind]
            store[ind] = max(nums[ind]+rob_houses(ind+2),rob_houses(ind+1))
            return store[ind]
        return max(rob_houses(0),rob_houses(1))
