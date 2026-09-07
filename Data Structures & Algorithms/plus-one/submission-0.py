class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for ind in range(len(digits)-1,-1,-1):
            res = carry+digits[ind]
            if res >= 10: carry = res//10
            else: carry = 0
            digits[ind] = res%10
        if carry > 0: 
            ans = [carry]
            for digit in digits: ans.append(digit)
            return ans
        else: return digits 