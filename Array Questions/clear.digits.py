# 3174. Clear Digits
"""
 you are given a string s.

Your task is to remove all digits by doing this operation repeatedly:

Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.

Input: s = "cb34"

Output: ""

Explanation:

First, we apply the operation on s[2], and s becomes "c4".

Then we apply the operation on s[1], and s becomes "".
"""

def clear_digit(s):
    """
    so we need to remove the number+chr with associated with it 
    if we analyse that 
    1. whenver their is a digit we need to remove the char 

    What if we use stack and implement this
    """

    st = []
    for c in s:
        if c.isdigit():
            st.pop()
        else:
            st.append(c)
    return "".join(st)

s = "abc23"
# out : a
s = "ab34"
# out : ''
