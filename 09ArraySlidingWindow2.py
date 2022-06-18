#%% 
# 674. Longest Continuous Increasing Subsequence

class Solution:
    def findLengthOfLCIS2(self, nums: list[int]) -> int:
        right = 1
        ans = count = 1

        while right < len(nums):
            if nums[right] > nums[right-1]:
                count += 1
            else:
                ans = max(ans, count)
                count = 1
            right += 1
        ans = max(ans, count)
        return ans

    def findLengthOfLCIS(self, nums: list[int]) -> int:
        ans = count = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                count = 1
            if count > ans:
                ans = count

        return ans

nums = [1,3,5,4,7]
nums = [2,2,2,2,2]
nums = [1,3,5,7]
Solution().findLengthOfLCIS(nums)
# %%
# 718. Maximum Length of Repeated Subarray

class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        left1 = left2 = 0
        ans = count = 0

        # while left1 < len(nums1) and left2 < len(nums2):
        #     if nums1[left1]:
        #         pass

nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
Solution().findLength(nums1, nums2)

# %%
# 1004. Max Consecutive Ones III

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        right = 0
        ans = 0
        remaining = k        

        while right < len(nums):
            while right < len(nums) and (nums[right] or remaining):
                if not nums[right]:
                    remaining -= 1
                right += 1

            ans = max(ans, right-left)

            if nums[left]:
                left += 1
            else:
                left += 1
                right += 1

        return ans

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
nums = [0,0,0,1]
k = 4
Solution().longestOnes(nums, k)
# %%
# 1658. Minimum Operations to Reduce X to Zero

class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:


nums = [1,1,4,2,3]
x = 5
Solution().minOperations(nums, x)

# %%
# 424. Longest Repeating Character Replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


s = "ABAB"
k = 2
Solution().characterReplacement(s, k)
# %%
# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring2(self, s: str) -> int:
        s_set = set()
        ans = 0
        left = 0
        right = 0

        while right < len(s):
            if s[right] not in s_set:
                s_set.add(s[right])
                right += 1
                ans = max(ans, right-left)
            else:
                s_set.remove(s[left])
                left+=1
            print(left, right, ans, s_set)
        return ans

    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        window = {}
        ans = 0

        while right < len(s):
            index = s[right]
            window[index] = window.get(index, 0) + 1

            while window[index] > 1:
                window[s[left]] -= 1
                left += 1
            
            ans = max(ans, right-left+1)
            right += 1
        return ans

s = "bcaabcbb"
s = "bbbbb"
s = "aab"
Solution().lengthOfLongestSubstring(s)

# %%
# 1695. Maximum Erasure Value

class Solution:
    def maximumUniqueSubarray2(self, nums: list[int]) -> int:
        left = 0
        right = 0
        ans = 0
        total = 0
        window = set()

        while right < len(nums):
            while right < len(nums) and nums[right] not in window:
                window.add(nums[right])
                total += nums[right]
                right += 1
            
            if total > ans:
                ans = total
            print(left, right, ans, total)
            
            while right < len(nums) and nums[right] in window:
                window.remove(nums[left])
                total -= nums[left]
                left += 1
        return ans
    
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        left = 0
        right = 0
        ans = 0
        total = 0
        window = set()

        while right < len(nums):
            if nums[right] not in window:
                window.add(nums[right])
                total += nums[right]
                right += 1
                if total > ans:
                    ans = total
            
            while right < len(nums) and nums[right] in window:
                window.remove(nums[left])
                total -= nums[left]
                left += 1
            
        return ans
    
nums = [4,2,4,5,6]
# nums = [5,2,1,2,5,2,1,2,5]
nums = [10000,1,10000,1,1,1,1,1,1]
Solution().maximumUniqueSubarray(nums)
# %%
# 1208. Get Equal Substrings Within Budget

class Solution:
    def equalSubstring2(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        right = 0
        count = 0
        ans = 0

        while right < len(s):
            cost = abs(ord(s[right])-ord(t[right]))
            if maxCost - cost >= 0:
                maxCost -= cost
                count += 1
                if count > ans:
                    ans = count
                right += 1
            else:
                maxCost += abs(ord(s[left])-ord(t[left]))
                count -= 1
                left += 1
        
        return ans

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        costs = [abs(ord(s[i])-ord(t[i])) for i in range(n)]

        left = 0
        right = 0
        window_sum = 0
        ans = 0

        while right < n:
            window_sum += costs[right]
            while window_sum > maxCost:
                window_sum -= costs[left]
                left += 1
            
            index = right - left + 1
            if index > ans:
                ans = index
            
            right += 1
        return ans

s = "abcd"
t = "bcdf"
maxCost = 3

s = "abcd"
t = "cdef"
maxCost = 3

s = "abcd"
t = "acde"
maxCost = 0
Solution().equalSubstring(s, t, maxCost)

# %%
# 1493. Longest Subarray of 1's After Deleting One Element

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        k = 1
        i = 0
        for j in range(len(nums)):
            k -= nums[j] == 0
            if k < 0:
                k += nums[i] == 0
                i += 1
        return j - i

    def longestSubarray2(self, nums: list[int]) -> int:
        left = 0
        right = 0
        window_count = 0
        ans = 0

        while right < len(nums):
            if nums[right] == 0:
                window_count += 1
            
            while window_count > 1:
                if nums[left] == 0:
                    window_count -= 1
                left += 1

            ans = max(ans, right-left)
            right += 1
        return ans

nums = [1,1,0,1]
nums = [0,1,1,1,0,1,1,0,1]
# nums = [1,1,1]
# nums = [1,1,0,0,1,1,1,0,1]
# nums = [0,0,0]
Solution().longestSubarray(nums)

# %%
# 795. Number of Subarrays with Bounded Maximum

class Solution:
    def numSubarrayMaxk(self, nums, k):
        count = 0
        ans = 0
        for n in nums:
            if n <= k:
                count += 1
            else:
                count = 0
            ans += count
        return ans

    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        return self.numSubarrayMaxk(nums, right) - self.numSubarrayMaxk(nums, left-1)

nums = [2,1,4,3]
left = 2
right = 3

nums = [2,9,2,5,6]
left = 2
right = 8

nums = [73,55,36,5,55,14,9,7,72,52]
left = 32
right = 69
Solution().numSubarrayBoundedMax(nums, left, right)
# %%
# 713. Subarray Product Less Than K

class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
        
        left = 0
        right = 0
        v_product = 1
        count = 0

        while right < len(nums):
            v_product *= nums[right]                

            while v_product >= k:
                v_product //= nums[left]
                left += 1

            count += right - left + 1
            right += 1

        return count

nums = [10,5,2,6]
k = 100
Solution().numSubarrayProductLessThanK(nums, k)
# %%
# 904. Fruit Into Baskets
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        trees = {}
        left = 0
        right = 0
        ans = 0

        while right < len(fruits):
            trees[fruits[right]] = trees.get(fruits[right], 0) + 1
            
            while len(trees) > 2:
                if trees[fruits[left]] > 1:
                    trees[fruits[left]] -= 1
                else:
                    del trees[fruits[left]]
                left += 1
            
            ans = max(ans, right-left+1)
            right += 1

        return ans

fruits = [1,2,1]
fruits = [0,1,2,2]
fruits = [1,2,3,2,2]
Solution().totalFruit(fruits)
# %%
# 1358. Number of Substrings Containing All Three Characters

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        str_dic = {}
        left = 0
        right = 0
        count = 0

        while right < len(s):
            str_dic[s[right]] = str_dic.get(s[right], 0) + 1

            while len(str_dic) == 3:
                count += len(s) - right
                if str_dic[s[left]] > 1:
                    str_dic[s[left]] -= 1
                else:
                    del str_dic[s[left]]
                left += 1
            
            right += 1
        return count

s = "abcabc"
# s = "aaacb"
Solution().numberOfSubstrings(s)

# %%
# 467. Unique Substrings in Wraparound String

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        p_set = set()
        left = 0
        right = 1
        count = 1

        while right < len(p):
            if [ord(p[right]) - ord(p[left])]%26 == 1:
                right += 1
                  
p = "zab"
Solution().findSubstringInWraproundString(p)