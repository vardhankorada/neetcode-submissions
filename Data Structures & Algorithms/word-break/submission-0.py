class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        store = {}
        def check_index(s,ind,dic):
            if ind in store.keys(): return store[ind]
            if ind >= len(s): return True
            for w in dic:
                if (ind+len(w)) <= len(s) and s[ind:ind+len(w)] == w:
                    store[ind] = check_index(s,ind+len(w),dic)
                    if store[ind]: return True
            store[ind] = False
            return False
        return check_index(s,0,wordDict)