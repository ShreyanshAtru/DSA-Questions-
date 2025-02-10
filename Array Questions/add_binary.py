# https://leetcode.com/problems/add-binary/description/
# Given two binary strings a and b, return their sum as a binary string.


def add_binary(a,b):
    """
     123
    +457
    ------
    1. we start the adding from the last digits 
    """
    a, b = a[::-1], b[::-1]
    ans = ''
    carry = 0

    for i in range(max(len(a), len(b))):
        A = int(a[i]) if i<len(a) else 0
        B = int(b[i]) if i<len(b) else 0

        total = A + B + carry
        chr = total%2
        ans = chr+ans
        carry = total//2
    if carry:
        ans = "1"+ans
    return ans
    

a = "11"
b = "01"

print(add_binary(a,b))

# ==================================================== by using built in functions

deimal_a = int(a,2)
deimal_b = int(b,2)

decinal_res = deimal_a+deimal_b
res = bin(decinal_res, 2)
print(res[2:])