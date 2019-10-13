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
    return nums

# A simple user interface to test the selection sort
nums = input("Enter a list of nums, using space between numbers\n").split(" ")
for i in range(len(nums)):
    nums[i] = int(nums[i])
nums = insertionSort(nums)
for i in range(len(nums)):
    nums[i] = str(nums[i])
print("The sorted list of nums is:")
print(" ".join(nums))
input("Press enter to leave")
