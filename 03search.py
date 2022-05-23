#%%
List = list

#%%
# 704. Binary Search
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = 0
        m = len(nums)-1
        index = -1
        while n<=m:
            index_now = (m-n)//2+n
            if nums[index_now] < target:
                n = index_now+1
            elif nums[index_now] > target:
                m = index_now-1
            else:
                return index_now
        return index

nums = [-1,0,3,5,9,12]
target = 9
Solution().search(nums, target)

# %%
# 374. Guess Number Higher or Lower
def guess(num: int) -> int:
    return 1 # 1 -1 0

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while True:
            num = (left+right)//2
            picked = guess(num)
            if picked == 1:
                left = num + 1
            elif picked == -1:
                right = num - 1
            else:
                return num

#%%
# 35. Search Insert Position

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return left

nums = [-1,0,3,5,9,12]
target = 9
nums = [1,3,5,6]
target = 7
Solution().searchInsert(nums, target)
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
# 167. Two Sum II - Input Array Is Sorted

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            val = numbers[left] + numbers[right]
            if val > target:
                right -= 1
            elif val < target:
                left += 1
            else:
                return [left+1, right+1]
    
numbers = [2,7,11,15]
target = 9
Solution().twoSum(numbers, target)

# %%
# 153. Find Minimum in Rotated Sorted Array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left+right)//2
            print(left, right, mid)
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
        

nums = [11,13,15,17]
Solution().findMin(nums)

# %%
# 154. Find Minimum in Rotated Sorted Array II
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid
                left += 1
            else:
                right -= 1
        
        return nums[right]

nums = [11,13,15,17]
Solution().findMin(nums)
# %%
# 33. Search in Rotated Sorted Array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1

nums = [4,5,6,7,0,1,2]
target = 8
nums = [3,1]
target = 1

Solution().search(nums, target)
# %%
# 81. Search in Rotated Sorted Array II
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return True
            elif nums[mid] > nums[left]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] < nums[left]:
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                left += 1
        
        return False

nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
target = 2

Solution().search(nums, target)

# %%

# 278. First Bad Version
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        while left < n:
            mid = (n+left)//2
            if isBadVersion(mid):
                n = mid
            else:
                left = mid + 1
        
        return left

# %%
# 162. Find Peak Element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        pass


#%%
# 852. Peak Index in a Mountain Array

class Solution:
    # def peakIndexInMountainArray(self, arr: List[int]) -> int:
    #     left = 0
    #     right = len(arr) - 1
    #     while left < right:
    #         mid = (left+right)//2
    #         if arr[mid-1] < arr[mid]:
    #             left = mid
    #         if arr[mid+1] < arr[mid]:
    #             right = mid

    #     return left

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left+right)//2
            if arr[mid] < arr[mid+1]:
                left = mid+1
            else:
                right = mid

        return left

arr = [0,1,0]
Solution().peakIndexInMountainArray(arr)
# %%
