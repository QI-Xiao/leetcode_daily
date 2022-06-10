# %%
# 875. Koko Eating Bananas

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        min_piles = 1
        max_piles = max(piles)

        while min_piles < max_piles:
            eat_time = 0
            mid = (min_piles+max_piles)//2
            for i in piles:
                if i <= mid:
                    eat_time += 1
                else:
                    eat_time += i//mid
                    if i%mid:
                        eat_time += 1
            
            if eat_time <= h:
                max_piles = mid
            else:
                min_piles = mid+1
        
        return min_piles


piles = [312884470]
h = 968709470
Solution().minEatingSpeed(piles, h)

# %%
# 209. Minimum Size Subarray Sum

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        size = len(nums)
        left = right = 0
        sum_lst = 0
        count = size + 1
        while right < size:
            sum_lst += nums[right]

            while sum_lst >= target:
                count = min(right-left+1, count)
                sum_lst -= nums[left]
                left += 1
            
            right += 1
        
        return count if count != size + 1 else 0

target = 7
nums = [2,3,1,2,4,3]
Solution().minSubArrayLen(target, nums)

# %%
# 658. Find K Closest Elements

class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        if x >= arr[-1]:
            return arr[-k:]
        elif x <= arr[0]:
            return arr[:k]
        else:
            left = 0
            right = len(arr)-1
            while right - left + 1 > k:
                if abs(x-arr[right]) >= abs(x-arr[left]):
                    right -= 1
                else:
                    left += 1
            return arr[left:right+1]

arr = [1,2,3,4,5]
k = 4
x = 3
Solution().findClosestElements(arr, k, x)

# %%
# 349. Intersection of Two Arrays

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()
        left_1 = left_2 = 0
        lst = []
        while left_1 < len(nums1) and left_2 < len(nums2):
            val_1 = nums1[left_1]
            val_2 = nums2[left_2]
            if val_1 == val_2:
                if val_1 not in lst:
                    lst.append(val_1)
                left_1 += 1
                left_2 += 1
            elif val_1 < val_2:
                left_1 += 1
            else:
                left_2 += 1
        return lst

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
Solution().intersection(nums1, nums2)

# %%
