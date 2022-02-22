"""
    LINKED LIST IMPLEMENTATION FROM SCRATCH
"""
# defining the node class
class NODE:
    def __init__(self, data):
        self.data = data # assigning value to the node
        self.next = None # initializing the next pointer

# defining the linked list class
class LINKEDLIST:
    def __init___(self):
        self.head = None # initializing the head with no data

## Driver code
if __name__ == '__main__':

# creating an instance of the linked list class
llist = LINKEDLIST()

llist.head = NODE(1) # assigning haed of the llist to the first node.
second = NODE(2) # assigning node 2 to the second
third = NODE(3)

llist.head.next = second
second.next =  third

