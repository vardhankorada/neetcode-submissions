class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low,high = 1, max(piles)
        min_until = max(piles)
        while low <= high:
            print(low,high)
            mid = (low+high)//2
            tot = 0
            for pile in piles: tot += math.ceil(pile/mid)
            if tot <= h:
                min_until = min(min_until,mid)
                high = mid-1
            else: low = mid+1
            print(tot)
        return min_until