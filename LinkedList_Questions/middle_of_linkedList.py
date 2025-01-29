# leetoce 876 
# https://leetcode.com/problems/middle-of-the-linked-list/

# solution first -> Better approach:

class Node:
    def __init__(self,data, next=None):
        self.data = data
        self.next = next

def middleNode(head):
    """
    if the length of list 
    1. odd -> middle will be n/2
    2. even -> n/2 + 1
    for both the cased we can write (len(arr)/2+1) 
    we'll first find out the length of list and will get the mid of this and then again a loop that
    will run in length of mid while we are increamention the head to next
    """

    if head is None and head.next is None:
        return head
    
    count = 0 
    temp = head 
    while temp:
        temp = temp.next
        count += 1
    mid = count //2 + 1

    temp = head

    while mid > 1:
        mid -= 1
        temp = temp.next
    
    return temp

#creating linkedlist and we'll pass the head of this 
head = Node(11)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

print(middleNode(head).data)



# ================================================\\===================================================>

# Optimal solution 2 
# will use tortoise hare algo

def middleNode2(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow 
