class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        for st in strs:
            tup = self.create_tup(st)
            if tup in store: store[tup].append(st)
            else: store[tup] = [st]
        return [val for key,val in store.items()]
    def create_tup(self,st):
        freq = [0]*26
        for ch in st:
            ind = ord(ch)-ord("a")
            freq[ind] += 1
        return tuple(freq)