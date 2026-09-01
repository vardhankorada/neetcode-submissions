class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(0,len(nums)-2):
            left,right = i+1,len(nums)-1
            tgt = -nums[i]
            while left < right:
                if nums[left]+nums[right] == tgt: 
                    ans.add((nums[i],nums[left],nums[right]))
                    left,right = left+1, right-1
                elif nums[left]+nums[right] < tgt: left += 1
                else: right -= 1
        return [list(tup) for tup in ans]