"""
pythonSort.py just runs the basic python sort funtion for educational purposes. It uses timsort which is a hybrid of merge sorting and insertion sorting. It is considered a fairly effective
    sorting method for almost all real world datasets.
Author: Joseph Tate
Version: 1.0
"""
nums = input("What numbers would you like to enter? \n")
nums = [int(i) for i in nums.split(" ")]
print(sorted(nums))
input("Type enter to exit")
