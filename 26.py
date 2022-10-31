class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        x=1
        for i in range(len(nums))
            if nums[i] != nums[i+1]:
                nums[x] = nums[i+1]
                x +=1
        return x

#Not in place(creates new array) also uses extra space(i guess :|)
    def removeDuplicates2(self, nums: list[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)


a=[0,0,1,1,1,2,2,3,3,4]

print(Solution().removeDuplicates(a))
