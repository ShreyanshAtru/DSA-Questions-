"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

# in hasmap we have to check the current num is there or not
# if yes, then check the index of current loop - index of that num[i]
# if above condition trus then return true
# if not then add the num in d
nums = [1,2,3,1], k = 3
d = {}
for i in range(len(nums)):
    if nums[i] in d and i - d[nums[i]] <= k:
        print(True)  # return True
        break
    d[nums[i]] = i  # nums : its index 
print(False)
