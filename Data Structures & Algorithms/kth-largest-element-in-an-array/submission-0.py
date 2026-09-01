class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = [num for num in nums[:k]]
        heapq.heapify(minheap)
        for num in nums[k:]:
            if num > minheap[0]: 
                heapq.heappop(minheap)
                heapq.heappush(minheap,num)
        return minheap[0]