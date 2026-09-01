class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = coins[::-1]
        store = {}
        def count_coins(coins,ind,tgt):
            if (ind,tgt) in store.keys(): return store[(ind,tgt)]
            if tgt == 0:
                return 0
            if ind >= len(coins) or tgt < 0:
                return float("inf")
            quo = tgt//coins[ind]
            min_count = float("inf")
            for i in range(0,quo+1):
                ans = i+count_coins(coins,ind+1,tgt-(i*coins[ind]))
                min_count = min(min_count,ans)
            store[(ind,tgt)] = min_count
            return min_count
        res =  count_coins(coins,0,amount)
        return res if res != float("inf") else -1
