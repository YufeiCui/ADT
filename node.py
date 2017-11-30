class Node(object):
    """
    A Class to represent a Node
    """

    def __init__(self: 'Node', data: object = None, next_node: 'Node' = None) -> None:
        self._data = data
        self._next = next_node

    @property
    def data(self: 'Node') -> object:
        return self._data

    @data.setter
    def data(self: 'Node', data: 'object') -> None:
        self._data = data

    @property
    def next(self: 'Node') -> 'Node':
        return self._next

    @next.setter
    def next(self: 'Node', next_node: 'object') -> None:
        self._next = next_node

    def __repr__(self: 'Node') -> str:
        return str(self.data)


if __name__ == '__main__':
    A = Node(1)
    B = Node(2)
    C = Node(3)

    A.next = B
    B.next = C
    C.next = None

    head = A
    while head is not None:
        print(head.data)
        head = head.next
