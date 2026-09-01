class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        store = {}
        def climb(ind):
            if ind >= len(cost)-2: return cost[ind]
            if ind in store.keys(): return store[ind]
            store[ind] = min(cost[ind]+climb(ind+1),cost[ind]+climb(ind+2))
            return store[ind]
        return min(climb(0),climb(1))