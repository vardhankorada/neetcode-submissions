class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre,post = [1],[1]
        for i in range(1,len(nums)): pre.append(pre[i-1]*nums[i-1])
        for i in range(len(nums)-2,-1,-1): post.append(post[len(nums)-2-i]*nums[i+1])
        return [pre[i]*post[len(pre)-1-i] for i in range(len(pre))]