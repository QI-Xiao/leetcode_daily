# %%
# 26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates2(self, nums: list[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i += 1

        return len(nums)

    def removeDuplicates(self, nums: list[int]) -> int:
        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow+1


nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
Solution().removeDuplicates(nums)

#%%
# 80. Remove Duplicates from Sorted Array II

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow = 0
        fast = 1
        only_one = True
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                only_one = True
                nums[slow] = nums[fast]
            elif only_one:
                only_one = False
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow+1

nums = [0,0,1,1,1,1,2,3,3]
Solution().removeDuplicates(nums)

# %%
# 27. Remove Element

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        fast = len(nums)-1
        slow = 0
        while slow < fast:
            if nums[fast] == val:
                fast -= 1
            else:
                if nums[slow] == val:
                    # nums[slow] = nums[fast]
                    fast -= 1
                slow += 1
        print(nums)
        return slow+1
                    

nums = [0,1,2,2,3,0,4,2]
val = 2
Solution().removeElement(nums, val)

#%%
# 845. Longest Mountain in Array

class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        res = 0
        for i in range(1,len(arr)-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                left = i - 1
                right = i + 1
                while left > 0 and arr[left] > arr[left-1]:
                    left -= 1
                while right < len(arr)-1 and arr[right] > arr[right+1]:
                    right += 1
                if right - left + 1 > res:
                    res = right - left + 1
        return res

arr = [2,1,4,7,3,2,5]
Solution().longestMountain(arr)

# %%
# 719. Find K-th Smallest Pair Distance
class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left+right)//2
            
# https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0719.%20%E6%89%BE%E5%87%BA%E7%AC%AC%20k%20%E5%B0%8F%E7%9A%84%E8%B7%9D%E7%A6%BB%E5%AF%B9.md


        
nums = [1,3,1]
k = 1
Solution().smallestDistancePair(nums, k)

# %%
# 334. Increasing Triplet Subsequence

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        a = float('inf')
        b = float('inf')

        for i in nums:
            if i < a:
                a = i
            elif i < b:
                b = i
            else:
                return True
        
        return False

nums = [1,2,3,4,5]
nums = [5,4,3,2,1]
Solution().increasingTriplet(nums)

# %%
# 978. Longest Turbulent Subarray

class Solution:
    def maxTurbulenceSize2(self, arr: list[int]) -> int:
        if len(arr) <= 1:
            return len(arr)
        total = 0
        num = 0
        turb_type = 0
        right = 1
        while right < len(arr):
            if arr[right-1] == arr[right]:
                num = 1
            elif (arr[right-1] > arr[right] and right%2) or (arr[right-1] < arr[right] and not right%2):
                if turb_type == 1:
                    num += 1
                else:
                    num = 2
                    turb_type = 1
            else:
                if turb_type == 2:
                    num += 1
                else:
                    num = 2
                    turb_type = 2
            # print(right, num, turb_type)
            right += 1

            if total < num:
                total = num
        return total

    def maxTurbulenceSize(self, arr: list[int]) -> int:
        left = 0
        right = 1
        ans = 1

        while right < len(arr):
            if arr[right-1] == arr[right]:
                left = right
            elif right != 1 and arr[right-2] > arr[right-1] and arr[right-1] > arr[right]:
                left = right - 1
            elif right != 1 and arr[right-2] < arr[right-1] and arr[right-1] < arr[right]:
                left = right - 1
            ans = max(ans, right-left+1)
            right += 1

        return ans

arr = [9,4,2,10,7,8,8,1,9]
Solution().maxTurbulenceSize(arr)

# %%
# 350. Intersection of Two Arrays II

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        dic1 = {}
        for i in nums1:
            if i in dic1:
                dic1[i] += 1
            else:
                dic1[i] = 1
        lst = []
        for num in nums2:
            if dic1.get(num):
                lst.append(num)
                dic1[num] -= 1
        return lst


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
Solution().intersect(nums1, nums2)

# %%
# 925. Long Pressed Name

class Solution:
    def isLongPressedName2(self, name: str, typed: str) -> bool:
        p = q = 0

        while p < len(name) and q < len(typed):
            char_name = name[p]
            char_len = 1
            while p+1 < len(name) and char_name == name[p+1]:
                p += 1
                char_len += 1
            typelen = 0
            while q < len(typed) and typed[q] == char_name:
                q+=1
                typelen+=1
            if typelen >= char_len:
                p+=1
            else:
                return False
        return p == len(name) and q == len(typed)

    def isLongPressedName(self, name: str, typed: str) -> bool:
        p = q = 0

        while p < len(name) and q < len(typed):
            if name[p] == typed[q]:
                p += 1
                q += 1
            elif p > 0 and typed[q-1] == typed[q]:
                q += 1
            else:
                return False

        while q < len(typed) and typed[q-1] == typed[q]:
            q += 1
        
        return True if p == len(name) and q == len(typed) else False


name = "saeed"
typed = "ssaaedd"
name = "alex"
typed = "aaleex"
name = "xnhtq"
typed = "xhhttqq"
name = "vtkgn"
typed = "vttkgnn"
Solution().isLongPressedName(name, typed)

# %%
# 844. Backspace String Compare

class Solution:
    def backspaceCompare2(self, s: str, t: str) -> bool:
        p = len(s)-1
        q = len(t)-1
        count_s_c = 0
        count_t_c = 0
        while p >= 0 and q >= 0:
            if s[p] == '#':
                p -= 1
                count_s_c += 1
            elif count_s_c:
                p -= 1
                count_s_c -= 1
            elif t[q] == '#':
                q -= 1
                count_t_c += 1

            elif count_t_c:
                q -= 1
                count_t_c -= 1
            else:
                if s[p] == t[q]:
                    p -= 1
                    q -= 1
                else:
                    return False
            # print(p, s[p], q, t[q], count_s_c, count_t_c)
        
        while p >= 0:
            if s[p] == '#':
                p -= 1
                count_s_c += 1
            elif count_s_c:
                p -= 1
                count_s_c -= 1
            else:
                return False

        while q >= 0:
            if t[q] == '#':
                q -= 1
                count_t_c += 1

            elif count_t_c:
                q -= 1
                count_t_c -= 1
            else:
                return False
        
        return True

    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(strs):
            lst = []
            for i in strs:
                if i != '#':
                    lst.append(i)
                elif lst:
                    lst.pop(-1)
            return lst
        
        return build(s) == build(t)


s = "ab##"
t = "c#d#"
s = "a#c"
t = "b"
Solution().backspaceCompare(s, t)

# %%
# 415. Add Strings

class Solution:
    def addStrings2(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        if n1 > n2:
            num2 = '0'*(n1-n2)+num2
            n = n1
        else:
            num1 = '0'*(n2-n1)+num1
            n = n2
        
        next_carry = 0
        rst = []
        for i in range(n-1,-1,-1):
            num = int(num1[i]) + int(num2[i]) + next_carry
            rst.append(str(num%10))
            next_carry = num//10

        if next_carry:
            rst.append(str(next_carry))
        
        return ''.join(rst[::-1])

    def addStrings(self, num1: str, num2: str) -> str:
        n1 = len(num1)-1
        n2 = len(num2)-1

        carry = 0
        lst = []

        while n1 >= 0 or n2 >= 0:
            if n1 < 0:
                num = int(num2[n2]) + carry
                n2 -= 1
            elif n2 < 0:
                num = int(num1[n1]) + carry
                n1 -= 1
            else:
                num = int(num1[n1]) + int(num2[n2]) + carry
                n1 -= 1
                n2 -= 1
            lst.append(str(num%10))
            carry = num//10
        
        if carry > 0:
            lst.append(str(carry))

        return ''.join(lst[::-1])

num1 = "1"
num2 = "9"

num1 = "11"
num2 = "123"
Solution().addStrings(num1, num2)

# %%
