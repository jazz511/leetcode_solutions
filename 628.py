import heapq


class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        l=sorted(nums)
        return max(l[0]*l[1]*l[-1] , l[-1]*l[-2]*l[-3])
        
        
def maximumProduct(self, nums: list[int]) -> int:
        b1,b2,b3, s1,s2,s3 = -2**32,-2**32, -2**32,2**32,2**32,2**32
        
        for n in nums:
            b1, b2, b3 = max(b1, n), max(b2, min(n, b1)), max(b3, min(b2, n))
            s1, s2, s3 = min(s1, n), min(s2, max(n, s1)), min(s3, max(s2, n))
        
        return max(s1*s2*s3, b1*b2*b3, s1*s2*b1)

def maximumProduct(self, nums):
        a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(a[0] * a[1] * a[2], b[0] * b[1] * a[0])