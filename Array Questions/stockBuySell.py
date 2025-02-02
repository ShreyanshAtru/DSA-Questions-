# Stock Buy and Sell – Multiple Transaction Allowed
# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/stock-buy-and-sell2615
"""
I need to check the first value and after that will be in increasing order,
if not then just pervious value minus first will be profit and increment the first ptr to next value
"""

arr = [100, 180, 260, 310, 40, 535, 695]
first = 0
second = 0
profit = 0

for i in range(1,len(arr)):
    if arr[i] > arr[i-1]:
        second = i
    else:
        profit += arr[second] - arr[first]
        first = i
        second = i
profit += arr[second] - arr[first]
print(profit)


# ============================================//========================================>
"""
What if only one transcatio allowed, means we can only buy one day and sell one day, no repeating buy-sell
"""

minPrice = float('inf') # first we set it positive infinity and will store the least number
maxPro = 0 # it'll be answer of the max profit we can get

for i in range(len(arr)):
    minPrice = min(minPrice, arr[i])
    maxPro = max(maxPro, arr[i]-minPrice)
print(maxPro)

# GFG
# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/buy-stock-2 

# Leetcode 
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/