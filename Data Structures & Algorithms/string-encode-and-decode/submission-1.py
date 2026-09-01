class Solution:

    def encode(self, strs: List[str]) -> str:
        for i,st in enumerate(strs):
            strs[i] = st+"||"
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        strs_list = s.split("||")
        return strs_list[:len(strs_list)-1]
