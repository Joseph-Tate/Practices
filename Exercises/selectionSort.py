"""
SelectionSort.py is a simple program that sorts a list of numbers based on selection sort algrorithms.
Author: Joseph Tate
Version: 1.0
"""
def selectionSort(nums):
    for i in range(len(nums)-1):
        # Finds index of smallest remaining element
        indexSmallest = i
        for j in range(i+1,len(nums)):
            if(nums[j] < nums[indexSmallest]):
                indexSmallest = j
        # Swaps nums[i] and nums[indexSmallest]
        nums[i], nums[indexSmallest] = nums[indexSmallest], nums[i]

    # Returns sorted nums
    return nums

# A simple user interface to test the selection sort
nums = input("Enter a list of nums, using space between numbers\n").split(" ")
for i in range(len(nums)):
    nums[i] = int(nums[i])
nums = selectionSort(nums)
for i in range(len(nums)):
    nums[i] = str(nums[i])
print("The sorted list of nums is:")
print(" ".join(nums))
input("Press enter to leave")
