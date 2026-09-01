class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        store = {}
        def climb(step):
            if step==len(cost)-1 or step==len(cost)-2: return cost[step]
            if step in store.keys(): return store[step]
            ans = cost[step]+min(climb(step+1),climb(step+2))
            store[step] = ans
            return ans
        return min(climb(0),climb(1))
