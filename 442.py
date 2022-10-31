class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        o=[]
        for i in nums:
            if nums[abs(i)-1] < 0:
                o.append(abs(i))
            else:
                nums[abs(i)-1] *= -1
        return o

a=[4,3,2,7,8,2,3,1]
print(Solution().findDuplicates(a))