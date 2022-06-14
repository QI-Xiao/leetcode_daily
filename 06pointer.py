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
        nums.sort()
        left = 0
        right = 1
        i = 2
        sum = 0
        while i < len(nums):

            if nums[left] + nums[right] > nums[i]:
                sum += right - left
                if right - left == 1:
                    i += 1
                    right = i - 1
                    left = 0
                else:
                    right -= 1
            else:
                if right - left == 1:
                    i += 1
                    right = i - 1
                    left = 0
                else:
                    left += 1
        return sum
    
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        sum = 0
        for i in range(2, len(nums)):
            left = 0
            right = i - 1

            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    sum += right - left
                    right -= 1
                else:
                    left += 1

        return sum
nums = [24,3,82,22,35,84,19]
Solution().triangleNumber(nums)

# %%
# 15. 3Sum
class Solution:
    def threeSum2(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        len_nums = len(nums)
        if len_nums < 3:
            return []
        print(nums)

        lst = []
        for i in range(len_nums-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len_nums - 1
            n_i = nums[i]
            print(i, left, right)
            while left < right:
                n_l = nums[left]
                n_r = nums[right]
                if n_i + n_l + n_r == 0:
                    print([n_i, n_l, n_r])
                    if [n_i, n_l, n_r] not in lst:
                        lst.append([n_i, n_l, n_r])
                    left += 1
                    right -= 1
                elif n_i + n_l + n_r > 0:
                    right -= 1
                else:
                    left += 1
        return lst

    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res

nums = [-2,0,0,2,2]
nums = [0,0,0,0]
Solution().threeSum(nums)

# %%
# 18. 4Sum

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()

        lst = []
        count = len(nums)
        for i in range(count-3):
            for j in range(i+1, count-2):
                left = j + 1
                right = count-1

                while left < right:
                    sum_4 = nums[i] + nums[j] + nums[left] + nums[right]
                    # print(i, j, left, right, sum_4)
                    if sum_4 > target:
                        right -= 1
                    elif sum_4 < target:
                        left += 1
                    else:
                        ret = [nums[i], nums[j], nums[left], nums[right]]
                        if ret not in lst:
                            lst.append(ret)
                        while left+1 < right and nums[left] == nums[left+1]:
                            left += 1
                        while right-1 > left and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                # print('-----------------------------')

        return lst

nums = [2,2,2,2,2]

target = 8
Solution().fourSum(nums, target)

# %%
# 16. 3Sum Closest

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        print(nums)

        rst = float('inf')
        for i in range(n-2):
            left = i+1
            right = n-1

            while left < right:
                sum_nums = nums[i] + nums[left] + nums[right]
                print(i, left, right, sum_nums, rst)
                if sum_nums - target < 0:
                    if abs(rst-target) > target - sum_nums:
                        rst = sum_nums
                    left += 1
                elif sum_nums - target > 0:
                    if abs(rst-target) > sum_nums - target:
                        rst = sum_nums
                    right -= 1
                else:
                    return target
            print()

        return rst

nums = [1,1,1,0]

target = -100
Solution().threeSumClosest(nums, target)

# %%
# 977. Squares of a Sorted Array

class Solution:
    def sortedSquares2(self, nums: list[int]) -> list[int]:
        index = -1
        for i in range(len(nums)):
            value = nums[i]
            if value < 0:
                index = i
            nums[i]= value * value

        print(nums, index)

        for i in range(index,-1,-1):
            tmp = nums[i]
            print()
            print('ttt', tmp)
            for j in range(i+1, len(nums)):
                print('j', j, 'nums[j]', nums[j])
                if tmp > nums[j]:
                    nums[j-1] = nums[j]
                    if j == len(nums)-1:
                        nums[j] = tmp
                else:
                    nums[j-1] = tmp
                    break
            print(nums)
        return nums

    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0
        index = right = len(nums)-1
        nums = [i**2 for i in nums]
        rst = [0 for _ in nums]

        while left <= right:
            if nums[left] > nums[right]:
                rst[index] = nums[left]
                left += 1
            else:
                rst[index] = nums[right]
                right -= 1
            index -= 1
        
        return rst

nums = [-5,-3,-2,-1]
Solution().sortedSquares(nums)

# %%
# 881. Boats to Save People

class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()

        left = 0
        right = len(people)-1
        count = 0

        while left <= right:
            if people[left]+people[right] <= limit:
                left += 1
            right -= 1
            count += 1

        return count

people = [3,2,2,1]
limit = 3
Solution().numRescueBoats(people, limit)

# %%
# 42. Trapping Rain Water

class Solution:
    def trap(self, height: list[int]) -> int:


height = [0,1,0,2,1,0,1,3,2,1,2,1]
Solution().trap(height)


# %%
# 443. String Compression

class Solution:
    def compress(self, chars: list[str]) -> int:
        left = right = 0

        while right < len(chars):
            chars[left] = chars[right]
            count = 1

            while right+1 < len(chars) and chars[right] == chars[right+1]:
                right += 1
                count += 1
            
            if count != 1:
                for c in str(count):
                    left += 1
                    chars[left] = c
            
            print(left, right, count, chars)

            right += 1
            left += 1

        print(chars)
        return left

chars = ["a","a","b","b","c","c","c"]
Solution().compress(chars)

# %%
