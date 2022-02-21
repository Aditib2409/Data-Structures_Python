"""
    IMPLEMENTATION OF STACKS - 4 DIFFERENT WAYS
        1. Lists
        2. collections.deque
        3. queue.LifoQueue
        4. Linked Lists
"""

# ---------------- LISTS ---------------- #

stack = []
L = 5 # size of the stack

for i in range(L):
    stack.append(i+1) # pushing elements into the stack

print('stack after pushing elemnts: ', stack)

# Pop elements from stack

print("Elements popped from the stack: ")
for i in range(L):
    print(stack.pop()) # elements are popped in the reverse order - FILO or LIFO

print("stack after popping the elements: ", stack) # should be empty as .pop() deletes the elements that are being popped 

# ----------------- collections.deque ------------------ #
# importing class deque from collections module
from collections import deque
#from turtle import st

stack = deque() # creating an object stack of the type deque
L = 5 # size of the stack

for i in range(L):
    stack.append(i+1)

print('stack after pushing elements: ', stack) # deque() type list

## Popping the elements from the stack
print("Elements popped from the stack: ")
for i in range(L):
    print(stack.pop()) # elements are popped in the reverse order - FILO or LIFO

print("stack after popping the elements: ", stack) # should be empty as .pop() deletes the elements that are being popped

# ---------------- queue.LifoQueue --------------- #

from queue import LifoQueue

stack = LifoQueue(maxsize=L)

for i in range(L):
    stack.put(i+1)

print('stack after pushing elements: ', stack) # LidoQueue() type list

## Popping the elements from the stack
print("Elements popped from the stack: ")
for i in range(L):
    print(stack.get()) # elements are popped in the reverse order - FILO or LIFO

print("stack after popping the elements: ", stack) # should be empty as .pop() deletes the elements that are being popped

# ------------ Linkedlist --------------- #

# node class
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# slack class
class Stack:
    # initializing stack with dummy node
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    # to check if the stack is empty
    def IsEmpty(self):
        return self.size == 0

    # to get the size of the stack
    def getSize(self):
        return self.size

    # push a val into the stack
    def push(self, val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    # pop the val from the end of the stack
    def pop(self):
        if self.IsEmpty():
            print("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.val


# driver mode - 
if __name__ == '__main__':
    stack = Stack()
    for i in range(L):
        stack.push(i+1) # pushing elements into the stack

    print(f"Elements of the Stack are:{stack}")

    # popping the elements
    for i in range(L):
        print(stack.pop())

    # the final stack must be empty.
    print("stack after popping all the elements: ", stack)