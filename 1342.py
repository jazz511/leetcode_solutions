class Solution:
    def numberOfSteps(self, num: int) -> int:
        s=0
        while num:
            s+=1
            if num%2 == 0:
                num = num/2
            else:
                num-=1
        return s

#Number of steps = number of divisions by 2 + number of subtractions = number of bitshifts + number of subtractions.
#Every non-zero binary number has a leading bit. The algorithm only stops when the leading bit is bitshifted enough to become the last bit and then it's subtracted by 1. Thus, number of bitshifts = number of bits that are not the leading bit = length of bitstring - 1. (Ex. 22 = 10110 requires 4 bitshifts for the number to become 1. 4 = length of bitstring - 1 = 5 - 1).

#As the number is shifted, each 1 eventually reaches the least significant bit position (the last, rightmost bit). A 1 in the last bit means the number is odd (which causes a subtraction), so the number of subtractions = number of 1s.

#number of steps = number of bitshifts + number of subtractions = (length of bitstring - 1) + number of 1s.

    def numberOfSteps2(self, num: int) -> int:
        bitstring = bin(num)[2:] # [2:] will remove the '0b' that is prepended to each bitstring by bin()
        return len(bitstring) - 1 + bitstring.count('1')

from time import time

start = time()
Solution().numberOfSteps(122357647893)
t1=time()
print(t1-start)
start=time()
Solution().numberOfSteps2(122357647893)
t1=time()
print(t1-start)
#print(Solution().numberOfSteps2(5))

