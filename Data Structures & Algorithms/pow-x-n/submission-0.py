class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n >= 0: return self.get_pow(x,n)
        return 1/self.get_pow(x,-n)

    def get_pow(self,x,n):
        if n == 1: return x
        if n == 0: return 1
        if n%2 == 0:
            ans = self.get_pow(x,n//2)
            return ans * ans
        else:
            ans = self.get_pow(x,(n-1)//2)
            return x * ans * ans