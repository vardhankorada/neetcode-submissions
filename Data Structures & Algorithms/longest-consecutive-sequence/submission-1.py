class Solution:
    # def longestConsecutive(self, nums: List[int]) -> int:
        # store = {}
        # for i,num in enumerate(nums): 
        #     if num not in store:store[num] = [i]
        #     else: store[num].append(i)
        # marked = [0]*len(nums)
        # max_len = 0
        # for i,num in enumerate(nums):
        #     if marked[i] == 1: continue
        #     curr = num
        #     ln = 0
        #     while curr in store:
        #         ln += 1
        #         for ind in store[curr]: marked[ind] = 1
        #         curr += 1
        #     max_len = max(ln,max_len)
        # return max_len
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ml = 0
        for num in nums:
            if num-1 in nums: continue
            ln = 0
            curr = num
            while curr in nums: 
                ln += 1
                curr += 1
            ml = max(ml,ln)
        return ml
