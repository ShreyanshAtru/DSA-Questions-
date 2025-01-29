class Node:

    def __init__(self, data, next=None):
        """
        using this consructor to create the Node
        """
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def travsel(self):          # print or shpwing linked list here
        if self.head is None:
            return "LinkedList is empty"

        itr = self.head
        s = ""
        while itr:
            s += str(itr.data) + "-->"
            itr = itr.next
        return s

    def insert_at_end(self, data):
        """
        end node next will always be Null/None
        we need to add the next of last element to new node
        """
        if self.head is None:
            self.head = Node(data, None)
            return 

        itr = self.head
        while itr.next:         
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, datalist):
        for data in datalist:
            self.insert_at_end(data)    # can also use insert_at_begining

    def get_length(self):
        count = 0
        if self.head is None:
            return 0
        
        itr = self.head

        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if self.head is None:
            return 
        
        if index == 0:
            return self.head
        count = 0
        itr = self.head

        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            count += 1

    def insert_at(self, index, data):
        if self.head is None:
            return self.head
        
        if index < 0 and index > self.get_length():
            return "Invalid index"
        
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                node = Node(data, itr.next)    # first we need to create the node, beacuse perious node contains next node ref
                itr.next = node         # here we are linking current node that is index-1 to the new node, by setting up its node reference to its next block
                break
            itr = itr.next
            count += 1

ll = LinkedList()
print(ll.insert_at_begining(1))
l = ["a", "b", "c"]
ll.insert_values(l)
ll.remove_at(2)
ll.insert_at(2, "new data")
print("linked list = ",ll.travsel())
print("Linkeded List Length =", ll.get_length())
