"""
    HEAP/PRIORITY QUEUE
        Heap - to represent 'Priority Queue'.
        using 'heapq' module
        FIFO
"""

import heapq
from urllib.request import HTTPPasswordMgrWithDefaultRealm

# creating a iterable - list
l = [1,2,3,4,5,6]

# converting the list into heap
heapq.heapify(l)

print("the heap: ", list(l))

# pushing an element into the heap
heapq.heappush(l, 7) # adds to the end of the queue

print("the modified heap: ", list(l))

# popping an element from the heap
print("Element popped out: ", heapq.heappop(l)) # removes from the front of the queue // returns 1

# final heap
print("After popping, the heap is: ", list(l))

# combining the functioning of both push and pop operations
print("pushes the element first and then pops: ", heapq.heappushpop(l,8))
print("heap is: ", list(l))

# first popping and then pushing the element
print("pops first pushes next: ", heapq.heapreplace(l,9))
print("heap is: ", list(l))

# to return the 'k' largest elements in the heap
print("3 largest elements in the heap: ", heapq.nlargest(3,l))

# return the 'k' smallest elements in the heap
print("2 smallest elements in the heap: ", heapq.nsmallest(2,l))