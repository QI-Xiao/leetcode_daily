# %%
# 167. Two Sum II - Input Array Is Sorted

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            num_now = numbers[left] + numbers[right]
            if num_now > target:
                right -= 1
            elif num_now < target:
                left += 1
            else:
                return [left+1, right+1]

numbers = [2,7,11,15]
target = 9
Solution().twoSum(numbers, target)

# %%
# 344. Reverse String

class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverseString2(self, s: list[str]) -> None:
        n = len(s)

        for i in range(n//2):
            s[i], s[n-i-1] = s[n-i-1], s[i]

s = ["h"]
Solution().reverseString2(s)
print(s)

# %%
# 345. Reverse Vowels of a String

class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s)-1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return ''.join(s)


s = "hello"
Solution().reverseVowels(s)

# %%
# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

s = "A man, a plan, a canal: Panama"
Solution().isPalindrome(s)

# %%
# 11. Container With Most Water

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        
        max_area = 0
        while left < right:
            if height[left] < height[right]:
                area = (right-left) * height[left]
                left += 1
            else:
                area = (right-left) * height[right]
                right -= 1
            if area > max_area:
                max_area = area
        return max_area

height = [1,8,6,2,5,4,8,3,7]
Solution().maxArea(height)

# %%
# 611. Valid Triangle Number

class Solution:
    def triangleNumber(self, nums: list[int]) -> int:



# %%
# 15. 3Sum
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        

nums = [-1,0,1,2,-1,-4]
Solution().threeSum(nums)

# %%
