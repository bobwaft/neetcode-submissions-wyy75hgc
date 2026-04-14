class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for i in operations:
            if (i not in ["+","C","D"]):
                stk.append(int(i))
            elif i == "+":
                temp = stk.pop()
                temp2 = temp + stk[-1]
                stk.append(temp)
                stk.append(temp2)
            elif i == "C":
                stk.pop()
            elif i == "D":
                temp = stk[-1]*2
                stk.append(temp)
        return sum(stk)