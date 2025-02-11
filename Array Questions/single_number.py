# https://leetcode.com/problems/single-number/description/
"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
"""
# XOR opertor feature
# Any number XORed with itself equals 0, i.e., a XOR a = 0.
# Any number XORed with 0 equals the number itself, i.e., a XOR 0 = a.

def single(nums):
    n = 0
    for i in range(len(nums)):
        n ^= nums[i]
    return n
