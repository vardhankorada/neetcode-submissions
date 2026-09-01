class Solution:
    def isValid(self, s: str) -> bool:
        store = {")":"(","}":"{","]":"["}
        stack = []
        for ch in s:
            if ch in "({[":stack.append(ch)
            else:
                if len(stack) == 0: return False
                if stack[-1] == store[ch]: stack = stack[:len(stack)-1]
                else: return False
        return len(stack)==0