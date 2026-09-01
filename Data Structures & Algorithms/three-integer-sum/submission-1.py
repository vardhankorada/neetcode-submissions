class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0,len(nums)-2):
            if nums[i] > 0 : break
            if i>0 and nums[i-1]==nums[i]: continue
            left,right = i+1,len(nums)-1
            tgt = -nums[i]
            while left < right:
                if nums[left]+nums[right] == tgt: 
                    ans.append([nums[i],nums[left],nums[right]])
                    left,right = left+1, right-1
                    while nums[left] == nums[left - 1] and left < right : left += 1
                elif nums[left]+nums[right] < tgt: left += 1
                else: right -= 1
        return ans