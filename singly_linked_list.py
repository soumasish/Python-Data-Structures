class SList:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, item):
        if not item:
            raise ValueError('Cannot add None item to a list')
        self.size += 1
        if self.root is None:
            self.root = Node(item)
        else:
            p = Node(item)
            p.next = self.root
            self.root = p

    """Remove the element at the specific index"""

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise ValueError('Index cannot be negative or greater than the size of the list')

        current = self.root
        if index == 0:
            self.root = self.root.next
        else:
            for _ in range(index - 1):
                current = current.next
            p = current.next.next
            if p is not None:
                current.next = p
            else:
                current.next = None

        self.size -= 1

    def __len__(self):
        return self.size

    def __repr__(self):
        return "[{}]".format(", ".join(map(str, self)))

    def __iter__(self):
        current = self.root
        while current is not None:
            yield current
            current = current.next


class Node:
    def __init__(self, data):
        if data is None:
            raise ValueError('Node cannot be instantiated without an item')
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)
