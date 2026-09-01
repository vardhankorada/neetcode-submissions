class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i,num in enumerate(nums):
            rem = target - num
            if rem in store: return [store[rem],i]
            store[num] = i