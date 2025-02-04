# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/

# sliding window approach

"""
s = 'xyzzaz'
possible str xyz, yzz, zza, zaz 

we need to find the str with len three those chr are distinct

this question also be something like with 'k' len not the fixed 3 
"""

s = 'xyzzaz'
k = 3
count = 0

for i in range(len(s)-k+1):
    s1 = s[i:i+k]
    d = {}          # in this we'll store the keys with the count of char

    for ch in s1:
        if ch in d:
            d[ch]+=1
        else:
            d[ch] = 1
        
    if len(d) == len(s1):
        count += 1

print(count)