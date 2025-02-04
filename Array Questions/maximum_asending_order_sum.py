# https://leetcode.com/problems/maximum-ascending-subarray-sum/description/
# Sliding window Approach 


"""
Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.

 

Example 1:

Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.
"""

nums = [10,20,30,5,10,50]

s = nums[0]         # let's suppose first sum 
ms = s              # let's suppose its the max sum in begining 

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        s += nums[i]
        ms = max(s, ms)
    else:
        s = nums[i]
        ms = max(s, ms)
print(ms)