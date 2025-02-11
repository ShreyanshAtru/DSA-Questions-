# https://leetcode.com/problems/missing-number/description/
"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Example 1:

Input: nums = [3,0,1]

Output: 2
"""

def missing(nums):
    n = len(nums)
    total_sum = int(n*(n+1)/2)
    missing = total_sum - sum(nums)
    return missing

