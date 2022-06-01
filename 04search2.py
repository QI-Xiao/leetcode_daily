#%%
# 69. Sqrt(x)

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        ans = -1
        while left <= right:
            mid = (left+right)//2
            if mid * mid > x:
                right = mid-1
            else:
                left = mid+1
                ans = mid

        return ans

Solution().mySqrt(81)

#%%
# 367. Valid Perfect Square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        while left <= right:
            mid = (left+right)//2
            if mid*mid > num:
                right = mid - 1
            else:
                left = mid + 1
                ans = mid

        return ans*ans == num

Solution().isPerfectSquare(81)

#%%
# 50. Pow(x, n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def cal(x, n):
            if n == 0:
                return 1
            elif n % 2:
                res = cal(x, n//2)
                return x * res * res
            else:
                res = cal(x, n//2)
                return res * res
        
        if n < 0:
            x = 1/x
            n = -n

        return cal(x, n)

Solution().myPow(0.44528, 0)

#%%
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            x = 1/x
            n = -n

        return x*self.myPow(x*x, n//2) if n%2 else self.myPow(x*x, n//2)

Solution().myPow(2.00000, 12)

#%%
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        
        res = 1

        while n:
            if n%2:
                res *= x
            x *= x
            n //= 2

        return res

Solution().myPow(2.00000, 2)

#%%



#%%
from random import shuffle

lst = [i for i in range(28)]
result = []
for i in range(1,50000):
    special = [i for i in range(7)]
    times = 0
    while len(special) > 0:
        shuffle(lst)
        special = [i for i in special if i not in lst[0:7]]
        times += 1
    result.append(times)


#%%
# print(result)
sum(result) / len(result)
# %%
