# 725. Split Linked List in Parts
# https://leetcode.com/problems/split-linked-list-in-parts/description/

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def splitListToParts(self, head, k):
        temp = head 
        count = 0
        while temp:
            count += 1
            temp = temp.next 
        temp = head 
        avg = count // k
        extra = count % k
        ans = [None]*k
        for i in range(k):
            if not temp: break
            curr = temp
            prev = None 
            length = 0

            while temp and length < avg:
                prev = temp
                temp = temp.next
                length += 1
            if extra > 0:
                prev = temp
                temp = temp.next 
                extra -= 1
            if prev:
                prev.next = None 
            ans[i] = curr
        return ans


"""
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.
"""