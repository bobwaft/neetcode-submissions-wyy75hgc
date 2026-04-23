class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        cache = {}
        for num in range(n+1):
            if num / 2 in cache:
                res.append(cache[num / 2])
            else:
                tmp = num
                count = 0
                while num > 0:
                    if num & 1 == 1:
                        count += 1
                    num = num >> 1
                cache[tmp] = count
                res.append(cache[tmp])
        print(cache)
        return res