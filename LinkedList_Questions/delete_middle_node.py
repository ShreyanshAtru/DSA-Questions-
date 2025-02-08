class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def delete_middle(self, head):
        if head is None and head.next is None and head.next.next is None:
            return head

        count = 0
        temp = head 
        while temp:
            count += 1
            temp = temp.next 
        mid = count //2

        if mid ==0:
            return head.next
        temp = head
        while mid>1:
            mid -= 1 
            temp = temp.next 
        temp.next = temp.next.next 

        return head.next
    
    def print_linked_list(self, head):
        temp = head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

#creating linkedlist and we'll pass the head of this 
head = Node(11)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

ll = Solution()
(ll.delete_middle(head))

print(ll.print_linked_list(head))