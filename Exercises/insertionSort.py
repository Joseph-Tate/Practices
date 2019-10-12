"""
insertionSort.py is project that sorts numbers using insertion sorting algorithms.
Author: Joseph Tate
Version: 1.0
"""
def insertionSort(nums):
    for i in range(len(nums)):
        j = i
        while(j > 0 and nums[j] < nums[j-1]):
            # Swaps nums[j] and nums[j-1]
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j-=1
    # Returns the sorted nums
