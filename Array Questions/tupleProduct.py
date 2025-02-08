# https://leetcode.com/problems/tuple-with-same-product/description/

"""
Tuple with Same Product

Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that
a * b = c * d where a, b, c, and d are elements of nums, 
and a != b != c != d.


Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
"""

def tupleProduct(nums):
    hashmap = {}
    # firstly will create a dict of product and its count
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            product = nums[i] * nums[j]
            if product in hashmap:
                hashmap[product] +=1
            else:
                hashmap[product] = 1
    ans = 0
    # now we will take that product which product count is equal to or greater to 2
    for key, value in hashmap.items():
        if value>=2:
            combination = (value * (value-1)) / 2
            ans = ans + int(combination)*8
    return ans