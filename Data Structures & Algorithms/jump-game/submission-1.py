class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        max_reach = 0
        for i,num in enumerate(nums):
            if num!=0: 
                max_reach = max(max_reach,i+num)
                if max_reach >= len(nums)-1: return True
            else:
                if max_reach > i: continue
                else: return False
        return False
