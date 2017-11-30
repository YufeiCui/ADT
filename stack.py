from node import Node


class EmptyStackException(Exception):
    pass


class Stack(object):
    """
    A Stack classes implemented with linked list
    """

    def __init__(self: 'Stack') -> None:
        self._top = None

    def push(self: 'Stack', data: object) -> None:
        # create a new Node and set its next to the previous top Node
        new_node = Node(data)
        new_node.next = self._top

        self._top = new_node

    def pop(self: 'Stack') -> object:
        if self.is_empty():
            raise EmptyStackException

        # retrieve the data and point top Node to the next Node in the linked list
        data = self._top.data
        self._top = self._top.next

        return data

    def is_empty(self: 'Stack') -> bool:
        return self._top is None

    def peak(self) -> object:
        if self.is_empty():
            raise EmptyStackException
        else:
            return self._top.data

    def __repr__(self: 'Stack') -> str:
        s = ""
        node = self._top

        while node is not None:
            s += str(node.data) + ", "
            node = node.next

        return s[:-2]
