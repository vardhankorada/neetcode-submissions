class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minUntil = prices[0]
        max_pro = 0
        for i in range(1,len(prices)): 
            minUntil = min(prices[i-1],minUntil)
            max_pro = max(prices[i]-minUntil,max_pro)
        return max_pro
