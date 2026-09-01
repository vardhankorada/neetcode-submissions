class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        st,et = {},{}
        for i in range(len(s)):
            st[s[i]] = st.get(s[i],0)+1
            et[t[i]] = et.get(t[i],0)+1
        return st == et
