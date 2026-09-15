class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        win_size = len(s1)
        start,end = 0,win_size-1
        dic1 = self.make_dic(s1)
        dic2 = self.make_dic(s2[start:end+1])
        while end < len(s2):
            if self.match(dic1,dic2): return True
            if dic2[s2[start]] == 1: del dic2[s2[start]]
            else: dic2[s2[start]] -= 1
            start,end = start+1,end+1
            if end >= len(s2): return False
            if dic2.get(s2[end],0) > 0 : dic2[s2[end]] += 1
            else: dic2[s2[end]] = 1
        return False

    def match(self,dic1,dic2):
        for k,v in dic1.items():
            if k in dic2.keys() and dic2[k] == v: continue
            else: return False
        for k,v in dic2.items():
            if k in dic1.keys() and dic1[k] == v: continue
            else: return False
        return True

    def make_dic(self,st):
        store = {}
        for s in st: store[s] = store.get(s,0)+1
        return store