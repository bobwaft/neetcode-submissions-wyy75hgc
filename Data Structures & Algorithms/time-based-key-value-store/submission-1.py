class TimeMap:

    def __init__(self):
        self.keyMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyMap:
            self.keyMap[key] = []
        self.keyMap[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyMap:
            return ""
        vals = self.keyMap[key]
        l,r = 0,len(vals) - 1
        while l<r:
            m = (l+r)//2
            if timestamp > vals[m][0]:
                l = m + 1
            elif timestamp < vals[m][0]:
                r = m - 1
            else:
                return vals[m][1]
        while l >= 0 and vals[l][0] > timestamp:
            l -= 1
        return "" if l <0 else vals[l][1]