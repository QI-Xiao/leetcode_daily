# https://www.programiz.com/dsa/bubble-sort

# %%
# Bubble Sort

def bubbleSort(array):
    for i in range(len(array)-1):
        for j in range(0, len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
        print(i, j, array)

data = [45, 11, 0, -2, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)

# %%
# Selection Sort Algorithm

def selectionSort(array, size):
    for step in range(size):
        min_idx = step

        for i in range(step+1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        
        array[step], array[min_idx] = array[min_idx], array[step]



data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)

# %%

# Insertion Sort Algorithm

def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = key

data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)

# %%
# Merge Sort Algorithm

def mergeSort(array):
    if len(array) > 1:
        r = len(array)//2
        L = array[:r]
        M = array[r:]
    
        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


array = [-2,3,-5]
mergeSort(array)
print(array)

# %%
# Quicksort Algorithm
def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = (array[high], array[i + 1])
    return i+1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi-1)
        quickSort(array, pi+1, high)

data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

quickSort(data, 0, len(data) - 1)

print('Sorted Array in Ascending Order:')
print(data)



# %%
# 283. Move Zeroes

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1

nums = [0,1,0,3,12]
Solution().moveZeroes(nums)

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


nums = [0,1,0,3,12]
Solution().moveZeroes(nums)

# %%
# 215. Kth Largest Element in an Array

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        for i in range(k):
            max_idx = i
            for j in range(i+1, len(nums)):
                if nums[j] > nums[max_idx]:
                    max_idx = j
            nums[max_idx], nums[i] = nums[i], nums[max_idx]

        return nums[i]

nums = [3,2,1,5,6,4]
k = 6
Solution().findKthLargest(nums, k)

# %%
# 75. Sort Colors

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        left = index = 0
        right = len(nums) - 1
        while index <= right:
            if nums[index] == 0:
                nums[index], nums[left] = nums[left], nums[index]
                left += 1
                index += 1
            elif nums[index] == 1:
                index += 1
            else:
                nums[index], nums[right] = nums[right], nums[index]
                right -= 1

            print(nums)
        print(nums)

nums = [2,0,1]
Solution().sortColors(nums)

# %%
# 88. Merge Sorted Array

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        index1 = m-1
        index2 = n-1
        index = m+n-1
        while index1 >= 0 and index2 >= 0:
            if nums1[index1] > nums2[index2]:
                nums1[index] = nums1[index1]
                index1 -= 1
            else:
                nums1[index] = nums2[index2]
                index2 -= 1
            index -= 1
        
        if index2 >= 0:
            nums1[0:index2+1] = nums2[0:index2+1]

        print(nums1)


Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3)
# Solution().merge([0], 0, [1], 1)

# %%
# 912. Sort an Array

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def merge(nums):
            if len(nums) > 1:
                r = len(nums)//2
                l = nums[:r]
                m = nums[r:]
                merge(l)
                merge(m)

                i = j = k = 0

                while i < len(l) and j < len(m):
                    if l[i] < m[j]:
                        nums[k] = l[i]
                        i += 1
                    else:
                        nums[k] = m[j]
                        j += 1
                    k += 1
                
                while i < len(l):
                    nums[k] = l[i]
                    i += 1
                    k += 1
                
                while j < len(m):
                    nums[k] = m[j]
                    j += 1
                    k += 1
            
        merge(nums)
        return nums

nums = [-2,3,-5]
Solution().sortArray(nums)

# %%
# Counting Sort

def countingSort(array):
    size = len(array)
    output = [0] * size

    count = [0] * 10

    for i in range(size):
        count[array[i]] += 1
    
    for i in range(1,10):
        count[i] += count[i-1]

    # print(array)
    # print(count)
    # print(output)
    # print()

    i = size - 1
    while i >= 0:
        # print(array[i], count[array[i]], count[array[i]]-1)
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1
    
    # print(output)
    # print(count)

    for i in range(0, size):
        array[i] = output[i]

data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)


# %%
# Radix Sort Algorithm

def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(size):
        index = array[i] // place
        count[index % 10] += 1
    
    for i in range(1, 10):
        count[i] += count[i-1]

    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index%10]-1] = array[i]
        count[index%10] -= 1
        i -= 1
    
    for i in range(size):
        array[i] = output[i]
    

def radixSort(array):
    max_element = max(array)

    place = 1

    # countingSort(array, place)
    # return

    while max_element // place > 0:
        countingSort(array, place)
        place *= 10


data = [121, 432, 564, 23, 1, 45, 788]
radixSort(data)
print(data)


# %%
# Bucket Sort Algorithm

def bucketSort(array):
    bucket = []

    # Create empty buckets
    for i in range(len(array)):
        bucket.append([])

    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)
    
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    
    return array

array = [.42, .32, .33, .52, .37, .47, .51]
print("Sorted Array in descending order is")
print(bucketSort(array))


# %%
