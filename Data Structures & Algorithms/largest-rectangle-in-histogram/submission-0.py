class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left = [-1]*len(heights)
        right = [len(heights)]*len(heights)
        stk = []
        for i in range(len(heights)):
            while stk and heights[stk[-1]] >= heights[i]:
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        stk = []
        for i in range(len(heights)-1,-1,-1):
            while stk and heights[stk[-1]] >= heights[i]:
                stk.pop()
            if stk:
                right[i] = stk[-1]
            stk.append(i)
        best = 0
        for i,height in enumerate(heights):
            best = max(best,height*(right[i]-left[i]-1))
        return best