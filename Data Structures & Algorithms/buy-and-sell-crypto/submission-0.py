class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minUntil = [max(prices)]
        for i in range(1,len(prices)): minUntil.append(min(prices[i-1],minUntil[i-1]))
        max_pro = 0
        for i in range(1,len(prices)): max_pro = max(prices[i]-minUntil[i],max_pro)
        return max_pro
