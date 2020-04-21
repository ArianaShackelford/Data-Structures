import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list_copy import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # queue = DoublyLinkedList()
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # add item to the back of queue
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        #remove and return item from the front of the queue
        if self.size is 0:
            None
        else:
            self.size -= 1
            self.storage.remove_from_head()

    def len(self):
        #should return the number of items in the queue
        return self.size
