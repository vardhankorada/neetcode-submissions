class Solution:
    def climbStairs(self, n: int) -> int:
        store = {}
        def climb(n):
            if n <= 2: return n
            if n-2 not in store.keys(): store[n-2] = climb(n-2)
            if n-1 not in store.keys(): store[n-1] = climb(n-1)
            return store[n-1]+store[n-2]
        return climb(n)