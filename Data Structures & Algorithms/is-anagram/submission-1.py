class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        store_one,store_two = {},{}
        for i in range(len(s)):
            store_one[s[i]] = store_one.get(s[i],0)+1
            store_two[t[i]] = store_two.get(t[i],0)+1
        for k,v in store_one.items():
            if k not in store_two.keys(): return False
            if store_one[k] != store_two[k]: return False
        for k,v in store_two.items():
            if k not in store_one.keys(): return False
        return True
        