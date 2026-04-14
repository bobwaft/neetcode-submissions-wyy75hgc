class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in s:
            if i in ["[","(","{"]:
                stk.append(i)
            elif stk:
                temp = stk.pop()
                if temp == "[" and i != "]":
                    return False
                elif temp == "{" and i != "}":
                    return False
                elif temp == "(" and i != ")":
                    return False
            else:
                return False
        return not stk