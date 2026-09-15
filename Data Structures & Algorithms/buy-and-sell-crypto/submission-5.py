class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start,end = 0,0
        max_profit = 0
        while end < len(prices):
            if start == end: end += 1
            elif prices[end] < prices[start]: start = end
            else:
                max_profit = max(max_profit,prices[end]-prices[start])
                end += 1
        return max_profit