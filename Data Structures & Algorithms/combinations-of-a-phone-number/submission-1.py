class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letterMap = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"],
        }

        res,cur = [],""
        self.helper(0,digits,cur,res,letterMap)
        return res
        

    def helper(self,i,digits,cur,res,letterMap):
        if i == len(digits):
            res.append(cur)
            return
        for j in range(len(letterMap[digits[i]])):
            tmp = cur + letterMap[digits[i]][j]
            self.helper(i+1,digits,tmp,res,letterMap)