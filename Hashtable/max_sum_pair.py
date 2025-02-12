# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description/

"""
You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

 

Example 1:

Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.
"""
nums = [18,43,36,13,7]
res = -1
d = {}
for n in nums:
    # Calculate the sum of digits for the current number i+j (1+8 for 18)
    total = sum(map(int, str(n)))
    # If the sum of digits has been seen before,
    # check if the current number contributes to a larger max sum
    if total in d:
        res = max(res, n+d[total])
    # Update the maximum number for the current digit sum
    d[total] = max(n, d[total])
print(res)