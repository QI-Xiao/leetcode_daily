#%%
# 66. Plus One
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        new_list = []
        while True:
            one = digits.pop()
            new_one = one + 1
            if new_one == 10:
                new_list.append(0)
                if not digits:
                    digits = [1]
                    break
            else:
                new_list.append(new_one)
                break
        new_list.reverse()
        return digits + new_list

print(Solution().plusOne([1,2,3]))

#%%
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits.insert(0,0)
        digits[-1] += 1
        for i in range(len(digits)-1, 0, -1):
            if digits[i] == 10:
                digits[i] = 0
                digits[i-1] += 1
            else:
                break
        
        if digits[0] == 0:
            digits.remove(0)
        
        return digits

print(Solution().plusOne([1,2,3]))

# %%
# 724. Find Pivot Index
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)

        sum_part = 0

        for i in range(len(nums)):
            if sum_part * 2 + nums[i] == total:
                return i
            sum_part += nums[i]
        return -1

Solution().pivotIndex(nums = [1,7,3,6,5,6])

# %%
# 485. Max Consecutive Ones
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        ans = 0
        sum = 0
        for num in nums:
            if num == 1:
                sum += 1
                ans = max(ans, sum)
            else:
                sum = 0
        return ans

#%%
# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        size = len(nums)
        res = [1 for _ in nums]

        left = 1
        for i in range(size):
            res[i] = left
            left *= nums[i]

        right = 1
        for i in range(size-1,-1,-1):
            res[i] *= right
            right *= nums[i]
        return res

Solution().productExceptSelf([1,2,3,4])

# %%
