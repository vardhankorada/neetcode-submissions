class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        store = set()
        def form_brackets(candidate,op,cl):
            if len(candidate) == 2*n:
                if op == cl: store.add(candidate)
                return
            if op == cl:
                pos = candidate + "("
                form_brackets(pos,op+1,cl)
            elif op > cl:
                pos_one = candidate + "("
                form_brackets(pos_one,op+1,cl)
                pos_two = candidate + ")"
                form_brackets(pos_two,op,cl+1)
            return
        form_brackets("(",1,0)
        return list(store)