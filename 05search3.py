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
# 1011. Capacity To Ship Packages Within D Days

class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        cap_min = max(weights)
        cap_max = sum(weights)

        while cap_min < cap_max:
            mid = (cap_min+cap_max)//2
            days_need = 1
            days_cap = 0

            for w in weights:
                if days_cap + w > mid:
                    days_need += 1
                    days_cap = 0
                days_cap += w

            # print(cap_min, cap_max, days_need,days,days_cap)

            if days_need <= days:
                cap_max = mid
            else:
                cap_min = mid+1

        return cap_min

# weights = [1,2,3,4,5,6,7,8,9,10]
# days = 5
weights = [3,3,3,3,3,3]
days = 2
Solution().shipWithinDays(weights, days)

# %%
# 1482. Minimum Number of Days to Make m Bouquets

class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        left = min(bloomDay)
        right = max(bloomDay)

        while left < right:
            mid = (left+right)//2
            m_now = 0
            k_now = 0

            for b in bloomDay:
                if b <= mid:
                    k_now += 1
                    if k_now == k:
                        k_now = 0
                        m_now += 1
                else:
                    k_now = 0
            print(left, right, mid, m_now)

            if m_now < m:
                left = mid + 1
            else:
                right = mid
            
        return left

class Solution2:
    def canMake(self, bloomDay, days, m, k):
        count = 0
        flower = 0
        for i in range(len(bloomDay)):
            if bloomDay[i] <= days:
                flower += 1
                if flower == k:
                    count += 1
                    flower = 0
            else:
                flower = 0
        return count >= m

    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m > len(bloomDay) / k:
            return -1

        left, right = min(bloomDay), max(bloomDay)

        while left < right:
            mid = left + (right - left) // 2
            if not self.canMake(bloomDay, mid, m, k):
                left = mid + 1
            else:
                right = mid

        return left

bloomDay = [1,10,3,10,2]
m = 3
k = 1

bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3

# bloomDay = [1,10,2,9,3,8,4,7,5,6]
# m = 4
# k = 2

Solution().minDays(bloomDay, m, k)
# %%
