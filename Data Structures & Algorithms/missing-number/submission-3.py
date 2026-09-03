class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(0,len(nums)): ans = (ans ^ i) ^ nums[i]
        return ans ^ len(nums)