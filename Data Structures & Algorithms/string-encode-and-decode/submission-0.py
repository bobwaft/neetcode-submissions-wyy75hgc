class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res+=str(len(str(len(i)))) # number of digits of length of word
            res+=str(len(i)) #length of word
            res+=i #word
        print(res)
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        while len(s) > 0:
            wordRes = ""
            lenRes = ""
            numDigits = int(s[0])
            s = s[1:]
            for digit in range(numDigits):
                lenRes += s[0]
                s = s[1:]
            lenRes = int(lenRes)
            for letter in range(lenRes):
                wordRes += s[0]
                s = s[1:]
            res.append(wordRes)
        return res
