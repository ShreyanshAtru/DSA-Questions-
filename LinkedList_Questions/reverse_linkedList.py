# Definition for singly-linked list.
# class Node:
#     def __init__(self, val=0, next=None):
#         self.data = data
#         self.next = next
class Solution:
    def reverseList(self, head):
        # stack = []
        # temp = head 
        # while temp:
        #     stack.append(temp.val)
        #     temp = temp.next
        # temp = head 
        # while temp:
        #     head.data = stack.pop()
        #     temp = temp.next
        # return head

        """
        [d1|ref1]-->[ d2 |ref2 ]-->[d3 | ref3]-->None
        we can reverse the ref by setting this 3 variables.
        1. prev, it'll set to be None to make head as End node
        2. current node is head 
        3. front node is current's next 

        Now the logic => 
        step 1. current.next's ref should be the prev {current.nect = prev}
        step 2. not we will increase the positions of these pointer
            prev = current
            current will be now one step forward 
            current = front 
        **step 3. we need to store front at start because we are swapping the
                    current's ref to with prev so its changing current's state
        ** step 4. As now at last our prev will be the head of reveresed list so return this 
        """

        current = head
        prev = None 

        while current:
            front = current.next 
            current.next = prev
            prev = current
            current = front
        return prev
    
    def print_linked_list(head):
        temp = head
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    
# head = Node(1)
# head.next = Node(3)
# head.next.next = Node(2)
# head.next.next.next = Node(4)

# ll = Solution
# ll.reverseList(head)
# print_linked_list(head)


# https://leetcode.com/problems/reverse-linked-list/