class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        prefMax = {}
        suffMax = {}
        prefMax[0] = height[0]
        for i in range(1,len(height)):
            prefMax[i] = max(prefMax[i-1],height[i])
            
        suffMax[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2,-1,-1):
            suffMax[i] = max(suffMax[i+1],height[i])
        
        for i in range(len(height)-1):
            res += min(prefMax[i],suffMax[i]) - height[i]
        return res