# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/

"""
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

"""

class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next 


class Solution:
    def binary_to_decimal(self, head):
        temp = head
        s = ''
        while temp:
            s = s + str(temp.data)
            temp = temp.next
        return int(s, 2)    # this will giev the decimal value 
    
    # another soltuon without using built-int method 

        ls = []
        while head:
            ls.append(head.data)
            head = head.data
        
        sum = 0
        a = 0
        for i in range(len(ls)-1, -1, -1):
            sum = sum + pow(2, a) * ls[i]
            a += 1
        return sum
