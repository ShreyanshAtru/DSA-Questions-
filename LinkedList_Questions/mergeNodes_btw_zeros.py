# https://leetcode.com/problems/merge-nodes-in-between-zeros/description/
"""
You are given the head of a linked list, which contains a series of integers separated by 0's.
The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node
whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

0->1->2->0->6->4->0
output node will be -> 3->10
"""

class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Solution:
    def sum_node(self, head):
        dnode = ListNode(0)
        temp = dnode 
        curr = head.next    # becasue the first node have zero value 

        s = 0 
        while curr:
            if curr.data != 0:
                s = s + curr.data
            else:
                temp.next = ListNode(s)
                temp = temp.next
                s = 0
            curr = curr.next 
        return dnode.next 
    
    def print_linkedList(self, head):
        s = ""
        while head:
            s += str(head.data) + '-->'
            head = head.next 
        print(s)
        

head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(0)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(0)

ll = Solution()
# print("before sum ", ll.print_linkedList(head))
new_head = ll.sum_node(head)
s = ""
while new_head:
    print(s)
    s += str(new_head.data) + '-->'
    new_head = new_head.next 
print(s)
# print("after the sum ")
# print(ll.print_linkedList(head))