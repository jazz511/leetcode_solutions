class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        def search(arr,low, high,target,skip_index):
            m=(low+high)//2
            if arr[m] == target and m != skip_index:
                print(m)
                return m
            elif low >= high:
                return -1
            elif arr[m] > target:
                return search(arr,low,m-1,target,skip_index)
            else:
                return search(arr,m+1,high,target,skip_index)
        
        length = len(nums)

        ## sorted arrays keys
        k=sorted(range(length), key=lambda x: nums[x])
        print(k)

        ##sorted array
        a=[nums[x] for x in k]
        print(a)
        for x in range(length):
            n=a[x]
            r=target-n
            i=search(a,0,length-1,r,x)
            print(x,r,n,i)
            if i > -1:
                return [k[x],k[i]]

a1=[2,7,11,15]
t1=9
a2=[3,2,4]
t2=6
a3=[0,3,-3,4,-1]
t3=-1
        
nums = [2,7,11,15]
target = 9
print(Solution().twoSum(a3,t3))