from Node import Node


class EmptyQueueException(Exception):
    pass


class Queue(object):
    """
    A Queue classes implemented with linked list
    """

    def __init__(self):
        self._head = Node()
        self._tail = Node()

    def enqueue(self: 'Queue', data):
        pass

    def dequeue(self):
        pass

    def is_empty(self):
        pass

    def peak(self):
        pass
