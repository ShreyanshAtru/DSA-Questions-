# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

"""
Given two strings s and part, perform the following operation on s
until all occurrences of the substring part are removed:

Find the leftmost occurrence of the substring part and remove it from s.
Return s after removing all occurrences of part.

A substring is a contiguous sequence of characters in a string.
"""

s = "eemckxmckx"
part = "emckx"

st = [] # will append all the character in stack
# but when the len(st) >= 3, we will check our part with last 3 chrs in stack.
m = len(part)

for ch in s:
    st.append(ch)
    
    if len(st) >= m:
        st_ch = "".join(st[-m:]) # in stack the abc will be "c", "b", "a" tp make abc we use negative index
        if st_ch == part:
            for r in range(m):
                st.pop()
print("".join(st)) 