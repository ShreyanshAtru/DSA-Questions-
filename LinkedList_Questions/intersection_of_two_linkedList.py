# https://leetcode.com/problems/intersection-of-two-linked-lists/

"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

a1-->a2-->         |
                   --> c1-->c2-->c3-->Null  
b1--> b2--> b3-->  |

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def intersectPair(self, headA, headB):
        len_a = self.getLength(headA)
        len_b = self.getLength(headB)

        curA = headA
        curB = headB
        while len_a > len_b:
            curA = curA.next
            lenA -= 1
        while len_a > len_a:
            curB = curB.next
            lenB -= 1

        while curA != curB:
            curA = curA.next
            curB = curB.next
        
        return curA
    

    def getLength(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count


# headA = [4,1,8,4,5] len = 5
# headB = [5,6,1,8,4,5] len= 6
# headB - headA = 1
# output intercet 8

