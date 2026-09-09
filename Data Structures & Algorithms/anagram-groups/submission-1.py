class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for st in strs:
            sign = self.get_signature(st)
            if sign in ans.keys(): ans[sign].append(st)
            else: ans[sign] = [st]
        return [v for k,v in ans.items()]

    def get_signature(self,st):
        sign = [0] * 26
        for let in st: sign[ord(let)-ord('a')] += 1
        return tuple(sign)