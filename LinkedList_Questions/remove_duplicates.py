class Node:
    def __init__(self,data, next=None):
        self.data = data
        self.next = next

class Solution:
    def remove_duplicates(self, head):
        """
        1, 2, 2 
        we can use two pointers, that will curr and prev
        curr : 2 (head's next)
        prev : 1 (head)
        now we will run the loop untill curr is None
        will check prev.val == cur.val => prev.next = cur.next 
        and will increase the one step of the pointers  
        """

        prev = head
        curr = head.next

        while curr is not None:
            if prev.data == curr.data:
                prev.next = curr.next
                prev=curr 
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return head
    
    def print_list(self, head):
        s = ""
        while head:
            s += str(head.data) + "-->"
            head = head.next
        print (s)


head = Node(1)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

ll = Solution()
print("before the removes ==>")
ll.print_list(head)
a = (ll.remove_duplicates(head))
ll.print_list(a)



# ===============================Another Approach=================>> 

def remove_duplicate(head):
    curr = head
    while curr.next and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

b = remove_duplicate(head)
ll.print_list(b)

# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# push
