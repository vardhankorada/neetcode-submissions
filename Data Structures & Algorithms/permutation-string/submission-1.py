class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) : return False
        st,en = 0,len(s1)-1
        h1,h2 = {},{}
        for i in range(len(s1)): h1[s1[i]] = h1.get(s1[i],0)+1
        flag = False
        while en < len(s2):
            curr = s2[st:en+1]
            if not flag:
                for i in range(len(s1)): h2[s2[i]] = h2.get(s2[i],0)+1
                flag = True
            else:
                h2[s2[en]] = h2.get(s2[en],0) + 1
                if h2[s2[st-1]] == 1: del h2[s2[st-1]]
                else: h2[s2[st-1]] = h2[s2[st-1]] - 1
            if h1== h2: return True
            st,en = st+1,en+1
        return False      