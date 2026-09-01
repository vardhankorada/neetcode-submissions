class Solution:
    def climbStairs(self, n: int) -> int:
        store = {}
        def climb(n):
            if n<=3: return n
            if n in store.keys(): return store[n]
            ans = climb(n-1)+climb(n-2)
            store[n] = ans
            return ans
        return climb(n)