class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = set()
        if len(s) == 0: return 0
        start,end = 0,0
        store.add(s[0])
        max_len = 0
        while end < len(s):
            if start == end: end += 1
            elif s[end] not in store:
                store.add(s[end])
                max_len = max(max_len,len(store))
                end += 1
            else:
                while s[end] in store:
                    store.remove(s[start])
                    start += 1
        return max_len