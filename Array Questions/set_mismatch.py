# https://leetcode.com/problems/set-mismatch/description/

"""
ou have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
"""

def check_duplicate(nums):
    d = {}
    for i in range(1,len(nums)+1):
        d[i] = nums.count(i)
    l = [0]*2
    for k,v in d.items():
        if v == 0:
            l[1] = k
        if v == 2:
            l[0] = k
    return l
    
nums = [1,2,2,4]
print(check_duplicate(nums))