class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbs = "+-*/"
        for token in tokens:
            if token in symbs:
                opb = stack.pop()
                opa = stack.pop()
                stack.append(self.perfOp(opa,opb,token))
            else: stack.append(int(token))
        return int(stack[-1])
    def perfOp(self,opa,opb,token):
        if token == "+": return opa + opb
        if token == "-": return opa - opb
        if token == "*": return opa * opb
        if token == "/":
            res = opa / opb
            if res < 0: return math.ceil(res)
            else: return math.floor(res)