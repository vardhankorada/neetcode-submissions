class Solution:
    def climbStairs(self, n: int) -> int:
        store = {}
        def climb(n):
            if n == 1: return 1
            if n == 2: return 2
            if n in store.keys(): return store[n]
            one_p = climb(n-1)
            two_p = climb(n-2)
            store[n] = one_p + two_p
            return store[n]
        return climb(n)