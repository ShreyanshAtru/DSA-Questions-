"""
You are given a 0-indexed integer array nums. A pair of integers x and y is called a strong pair 
if it satisfies the condition:
|x - y| <= min(x, y)
You need to select two integers from nums such that they form a strong pair and 
their bitwise XOR is the maximum among all strong pairs in the array.
"""

nums = [1,1,10,3,9]
maxor = 0
for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
            maxor = max(maxor, nums[i]^nums[j])
print(maxor)


# https://leetcode.com/problems/maximum-strong-pair-xor-i/description/
