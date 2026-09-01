class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) : return False
        st,en = 0,len(s1)-1
        while en < len(s2):
            curr = s2[st:en+1]
            ans = self.checkPerm(curr,s1)
            if ans: return True
            st,en = st+1,en+1
        return False

    def checkPerm(self,s1,s2):
        h1,h2 = {},{}
        for i in range(len(s1)):
            h1[s1[i]] = h1.get(s1[i],0)+1
            h2[s2[i]] = h2.get(s2[i],0)+1
        return h1==h2        