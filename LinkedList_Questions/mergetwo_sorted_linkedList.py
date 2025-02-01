class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Solution:
    def merge(self, head, head2):
        """
        we're changing the links between the nodes 
        dummy node is using to show the head of the node 
        """
        dnode = Node(-1)
        temp = dnode
        t1 = head
        t2 = head2


        while t1 is not None and t2 is not None:   # head and head2
            # if head.data <= head2.data:
            #     temp.next = head
            #     head = head.next
            # else:
            #     temp.next = head2
            #     head2 = head2.next
            # temp = temp.next
            if t1.data < t2.data:
                temp.next = t1
                temp = t1
                t1 = t1.next
            else:
                temp.next = t2
                temp = t2
                t2 = t2.next
        if t1:
            temp.next = t1
        else:
            temp.next = t2
        return dnode.next
    
    def print_list(self, new_head):
        temp = new_head
        s = ""
        while temp is not None:
            s += str(temp.data) + "-->"
            print(s)
            temp = temp.next
        print(s)
        return s



head = Node(1)
head.next = Node(2)
head.next.next = Node(4)

head2 = Node(1)
head2.next = Node(3)
head2.next.next = Node(4)

ll = Solution()

print(ll.print_list(head))
new_head = ll.merge(head, head2)


print(ll.print_list(new_head))



# https://leetcode.com/problems/merge-two-sorted-lists/
# merge two sorted linked Lists 

