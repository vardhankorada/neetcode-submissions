class Solution:
    def rob(self, nums: List[int]) -> int:
        store = {}
        def solve(nums,ind):
            if ind > len(nums)-1: return 0
            if ind in store: return store[ind]
            ans = max(solve(nums,ind+1),nums[ind]+solve(nums,ind+2))
            store[ind] = ans
            return ans
        return solve(nums,0)
        