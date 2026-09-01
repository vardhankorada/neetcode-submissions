class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        store = {}
        def climb(ind):
            # if ind == len(cost): return 0
            if ind == len(cost)-1 or ind == len(cost)-2: return cost[ind]
            if ind in store.keys(): return store[ind]
            one_jump = cost[ind]+climb(ind+1)
            two_jump = cost[ind]+climb(ind+2)
            store[ind] = min(one_jump,two_jump)
            return store[ind]
        return min(climb(0),climb(1))