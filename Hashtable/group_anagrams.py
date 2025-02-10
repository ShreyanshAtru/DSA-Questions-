# https://leetcode.com/problems/group-anagrams/description/
# leet code - 49 

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

from collections import defaultdict

def group_anagram(strs):
    """
     intializing this defaultdict to avoid a edge case where in 
        first this res is rempty 
        the core ieda is that
        for each sorted key, we will append the str
    """

    res = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        res[key].append(s)
    return list(res.values())


# ================================= without using sorted function 
"""
If we don't have to use sorted method then we'll do this by 
ascii value 
ord(c) - ord('a) 
"""
strs = ["eat","tea","tan","ate","nat","bat"]
hash_map = defaultdict(list)

for w in strs:
    abc = [0] * 26
    for c in w:
        abc[ord(c) - ord("a")] += 1     # getting the 
    x = tuple(abc)  # list keys must be unmutable 
    hash_map[x].append(w)
print([arr for arr in hash_map.values()])
