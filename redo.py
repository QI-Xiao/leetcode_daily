# %%
# 34. Find First and Last Position of Element in Sorted Array

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def search(target):
            left, right = 0, len(nums)
            while left < right:
                mid = (left+right)//2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        lo = search(target)
        hi = search(target+1)-1
        print(lo, hi)

        if lo <= hi:
            return [lo, hi]

        return [-1,-1]


nums = [1]
target = 1
Solution().searchRange(nums, target)
# %%
