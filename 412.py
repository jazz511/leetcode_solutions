class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        a=[]
        for i in range(1,n+1):
            x=1
            a.append("")
            if i%3 == 0:
                a[i-1] += "Fizz"
                x=0
            if i%5 == 0:
                a[i-1] += "Buzz"
                x=0
            if x: a[i-1] = str(i)
        return a

## Oneliner list compressions
return [ 'Fizz' * (not i % 3) + 'Buzz' * (not i % 5 ) or str(i) for i in range(1, n+1) ]

print(Solution().fizzBuzz(3))
