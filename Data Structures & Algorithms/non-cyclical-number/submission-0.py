class Solution:
    def isHappy(self, n: int) -> bool:
        prev = set()
        while n!= 1:
            n = self.sumofSquares(n)
            if n not in prev: prev.add(n)
            else: return False
        return True
        
    def sumofSquares(self,n):
        digits = self.getDigits(n)
        return sum([x**2 for x in digits])

    def getDigits(self,n):
        digits = []
        while n != 0:
            digits.append(n%10)
            n = n // 10
        return digits