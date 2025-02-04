# stack implementation using Linked List
# linked List all about address mapping nothing more than that

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_add = Node(data)
            new_add.next = self.head
            self.head = new_add
        
    def pop(self):
        if self.head is None:
            return "empty stack"
        
        while self.head:
            pop_data = self.head.data
            self.head = self.head.next
            return pop_data
    
    def print_stack(self):
        if self.head is None:
            return "empty stack"

        while self.head:
            print(self.head.data)
            self.head = self.head.next


stack_obj = Stack()
stack_obj.push(1)
stack_obj.push(10)
stack_obj.push(100)

stack_obj.pop()
stack_obj.print_stack()




