# %%
# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        count = left = 0
        right = k
        target = threshold * k
        total = sum(arr[left:right])

        while right <= len(arr):
            print(right, left, total, target, count)
            if total >= target:
                count += 1
            if right < len(arr):
                total += arr[right] - arr[left]
            right += 1
            left += 1
        
        return count

arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
Solution().numOfSubarrays(arr, k, threshold)

# %%
# 643. Maximum Average Subarray I

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        left = 0
        right = k
        total = biggest = sum(nums[left:right])
        
        while right < len(nums):
            total = total + nums[right] - nums[left]
            if total > biggest:
                biggest = total

            right += 1
            left += 1
        
        return biggest/k


nums = [1,12,-5,-6,50,3]
k = 4
nums = [9,7,3,5,6,2,0,8,1,9]
k = 6
Solution().findMaxAverage(nums, k)

# %%
# 1052. Grumpy Bookstore Owner

class Solution:
    def maxSatisfied2(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        n = len(customers)
        satified = un_satified = 0
        
        left = 0
        right = minutes

        for i in range(n):
            if grumpy[i] == 0:
                satified += customers[i]
            else:
                if i < right:
                    un_satified += customers[i]

        max_un_sat = un_satified
        while right < n:
            un_satified = un_satified + (customers[right] if grumpy[right] else 0) - (customers[left] if grumpy[left] else 0)

            if un_satified > max_un_sat:
                max_un_sat = un_satified

            left += 1
            right += 1

        return satified + max_un_sat

    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        left = right = count = ans = satified = 0

        while right < len(customers):
            if grumpy[right] == 1:
                count += customers[right]
            else:
                satified += customers[right]

            if right-left+1 > minutes:
                if grumpy[left] == 1:
                    count -= customers[left]
                left += 1

            right += 1

            if count > ans:
                ans = count
            
        return satified + ans

custom = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3
Solution().maxSatisfied(custom, grumpy, minutes)

# %%
# 1423. Maximum Points You Can Obtain from Cards

class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        left = 0
        right = k
        total = ans = sum(cardPoints[left:right])

        while right > 0:
            left -= 1
            right -= 1
            total = total + cardPoints[left] - cardPoints[right]
            if total > ans:
                ans = total

        return ans

cardPoints = [1,2,3,4,5,6,1]
k = 3
Solution().maxScore(cardPoints, k)
# %%
# 1456. Maximum Number of Vowels in a Substring of Given Length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = right = count = ans = 0
        vowels = ['a', 'e', 'i', 'o', 'u']

        while right < len(s):
            if s[right] in vowels:
                count += 1

            if right - left + 1 > k:
                if s[left] in vowels:
                    count -= 1
                left += 1

            right += 1

            if count > ans:
                ans = count
                if ans == k:
                    return ans

        return ans

s = "abciiidef"
k = 3
Solution().maxVowels(s, k)
# %%
# 567. Permutation in String
import collections

class Solution:
    def checkInclusion1(self, s1: str, s2: str) -> bool:
        s1_count = collections.Counter(s1)

        left = right = 0

        window_count = collections.Counter()
        window_size = len(s1)

        while right < len(s2):
            window_count[s2[right]] += 1

            if right - left + 1 >= window_size:
                if window_count == s1_count:
                    return True
                window_count[s2[left]] -= 1
                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]
                left += 1
            right += 1
        return False

    def checkInclusion2(self, s1: str, s2: str) -> bool:
        s1_count = {}
        for i in s1:
            s1_count[i] = s1_count.get(i,0) + 1

        left = right = 0
        window_size = len(s1)
        s2_count = {}

        while right < len(s2):
            s2_count[s2[right]] = s2_count.get(s2[right], 0) + 1

            if right - left + 1 >= window_size:
                if s1_count == s2_count:
                    return True
                s2_count[s2[left]] -= 1
                if s2_count[s2[left]] == 0:
                    del s2_count[s2[left]]
                left += 1
            right += 1

        return False
            
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapp = [0] * 26
        for c in s1:
            mapp[ord(c)-97] += 1
        left = right = 0
        count_chars = n = len(s1)

        while right < len(s2):
            if mapp[ord(s2[right])-97] > 0:
                count_chars -= 1
            mapp[ord(s2[right])-97] -= 1
            right += 1
            if count_chars == 0:
                return True
            if right - left == n:
                if mapp[ord(s2[left])-97] >= 0:
                    count_chars += 1
                mapp[ord(s2[left])-97] += 1
                left += 1
        return False

s1 = "ab"
s2 = "eidbaooo"
Solution().checkInclusion(s1, s2)

# %%
# 438. Find All Anagrams in a String

class Solution:
    def findAnagrams2(self, s: str, p: str) -> list[int]:
        chars_lst = [0]*26
        for c in p:
            chars_lst[ord(c)-97] += 1

        p_len = n = len(p)
        right = 0
        lst = []

        for left in range(len(s)-n+1):
            while right - left < n:
                if chars_lst[ord(s[right])-97] > 0:
                    p_len -= 1
                chars_lst[ord(s[right])-97] -= 1

                right += 1
            
            if p_len == 0:
                lst.append(left)

            index = ord(s[left])-97
            if chars_lst[index] >= 0:
                p_len += 1
            chars_lst[index] += 1
            left += 1
        
        return lst

    def findAnagrams(self, s: str, p: str) -> list[int]:
        need = {}
        for ch in p:
            need[ch] = need.get(ch, 0) + 1

        window = {}
        window_size = len(p)

        ans = []
        left = right = valid = 0

        while right < len(s):
            ch_right = s[right]
            if ch_right in need:
                window[ch_right] = window.get(ch_right, 0) + 1
                if window[ch_right] == need[ch_right]:
                    valid += 1
            
            ch_left = s[left]
            if right - left + 1 == window_size:
                if valid == len(need):
                    ans.append(left)
                if ch_left in need:
                    if window[ch_left] == need[ch_left]:
                        valid -= 1
                    window[ch_left] -= 1
                left += 1
            right += 1
        
        return ans

s = "abcabc"
p = "abc"
Solution().findAnagrams(s, p)

# %%
# 995. Minimum Number of K Consecutive Bit Flips

class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        pass

nums = [0,1,0]
k = 1
Solution().minKBitFlips(nums, k)
