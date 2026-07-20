class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            targ = -nums[i]
            if targ < 0:
                break
            l,r = i+1,len(nums)-1
            while l < r:
                if nums[l] + nums[r] > targ:
                    r -= 1
                elif nums[l] + nums[r] < targ:
                    l += 1
                else:
                    if [nums[i],nums[l],nums[r]] not in res:
                        res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
        return res