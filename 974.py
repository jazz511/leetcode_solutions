class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        ans = 0
        d = {0: 1}
        _len = len(nums)
        acc = 0
        for i in range(_len):
            acc += nums[i]
            key = acc % k

            if key in d:
                ans += d[key]
                d[key] += 1
            else:
                d[key] = 1
        return ans

#optmized - replace dictionary with list:
    def subarraysDivByK2(self, nums: list[int], k: int) -> int:
        res = 0
        d = [1] + [0] * k # range of key is 0 <= key < K because key always mod by K
        acc = 0
        for a in nums:
            acc = (acc + a) % k # it's works because a % k % k % k .... n times is still same as a % k
            if d[acc]:
                res += d[acc]
            d[acc] += 1
        return res

a=[4,5,1,1,1,1,1]
print(Solution().subarraysDivByK(a,5))
