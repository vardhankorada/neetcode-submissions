class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        stored = {}
        ind = 0
        while ind < k:
            dist = -pow(pow(points[ind][0],2)+pow(points[ind][1],2),0.5)
            if dist not in stored.keys(): 
                stored[dist] = []
                heapq.heappush(minheap,dist)
            stored[dist].append(points[ind])
            ind += 1
        for point in points[ind:]:
            dist = -pow(pow(point[0],2)+pow(point[1],2),0.5)
            if dist > minheap[0]: 
                to_rem = heapq.heappop(minheap)
                del stored[to_rem]
                if dist not in stored.keys(): stored[dist] = [point]
                else: stored[dist].append(point)
                heapq.heappush(minheap,dist)
        ans = []
        for key,val in stored.items():
            for pt in val: ans.append(pt)
        return ans