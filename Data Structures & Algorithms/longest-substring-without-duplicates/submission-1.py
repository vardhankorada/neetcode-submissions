class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        store = set()
        store.add(s[0])
        l,r = 0,1
        max_len = 1
        while l < r and r < len(s):
            # print(store,max_len)
            if s[r] not in store:
                store.add(s[r])
                max_len = max(max_len,len(store))
                r += 1
            else:
                while l <r and s[r] in store:
                    store.remove(s[l])
                    l += 1
                if l == r: 
                    store.add(s[l])
                    r+= 1
        return max_len
