class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r=w=0
        for i in range(len(nums)):
            e=nums.pop(i)
            if e == 0:
                 nums.insert(0,e)
                 r+=1
            elif e == 1:
                 nums.insert(r,e)
                 w+=1
            else:
                 nums.insert(r+w,e)
        print(nums)

nums = [2,0,2,1,1,0]

Solution().sortColors(nums)