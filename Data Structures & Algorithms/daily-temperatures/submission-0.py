class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = [(temps[0],0)]
        res = [0 for i in range(len(temps))]
        for i in range(1,len(temps)):
            temp = temps[i]
            while stack and temp > stack[-1][0]:
                top = stack.pop()
                res[top[1]] = i-top[1]
            stack.append((temp,i))
        return res