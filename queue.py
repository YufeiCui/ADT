from node import Node


class EmptyQueueException(Exception):
    pass


class Queue(object):
    """
    A Queue classes implemented with linked list
    """

    def __init__(self: 'Queue') -> None:
        self._head = None
        self._tail = None

    def enqueue(self: 'Queue', data: object) -> None:
        # create a Node with value of data
        new_node = Node(data)

        # set tail.next to data if it exists
        if self._tail:
            self._tail.next = new_node

        # set the tail to the new data
        self._tail = new_node

        # if head is None, then point to data as well
        if not self._head:
            self._head = new_node

    def dequeue(self: 'Queue') -> object:
        if self.is_empty():
            raise EmptyQueueException

        # get the data and move the head to head.next
        data = self._head.data
        self._head = self._head.next

        return data

    def is_empty(self: 'Queue') -> bool:
        return self._head is None

    def peak(self: 'Queue') -> object:
        if self.is_empty():
            raise EmptyQueueException
        else:
            return self._head.data

    def __repr__(self: 'Queue') -> str:
        s = ""
        node = self._head

        while node is not None:
            s += str(node.data) + ", "
            node = node.next

        return s[:-2]
