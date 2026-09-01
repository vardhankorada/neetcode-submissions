class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        ans = 0
        flag = False
        for num in nums:
            if num > 0: flag = True
            if curr < 0: curr = 0
            curr += num
            ans = max(ans,curr)
        if not flag: return max(nums)
        return ans