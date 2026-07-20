class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for c in tokens:
            if c == "+":
                n1 = stk.pop()
                stk.append(stk.pop()+n1)
            elif c == "-":
                n1 = stk.pop()
                stk.append(stk.pop()-n1)
            elif c == "*":
                n1 = stk.pop()
                stk.append(stk.pop()*n1)
            elif c == "/":
                n1 = stk.pop()
                n2 = stk.pop()
                stk.append(int(n2/n1))
            else:
                stk.append(int(c))
        return stk[0]