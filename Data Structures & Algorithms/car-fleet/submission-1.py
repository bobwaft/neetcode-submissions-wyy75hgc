class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []
        for i in range(len(position)):
            combined.append((position[i],speed[i]))
        combined.sort()
        stk = []
        for i,(pos,speed) in enumerate(combined):
            time = (target-pos)/speed
            print(time)
            while stk and stk[-1] <= time:
                stk.pop()
            stk.append(time)
        return len(stk)