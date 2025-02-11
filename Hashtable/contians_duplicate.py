# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/description/

"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Input: nums = [1,2,3,1]

Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.
"""

def check_any_dulicate(nums):
    d = {}
    for i in range(len(nums)):
        if nums[i] in d:
            d[nums[i]] += 1
        else:
            d[nums[i]] = 1
        if d[nums[i]] >=2:
            return True
    return False

# Secon approach is that -> len(set(nums)) != len(nums) => True