class DList:

    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, data):
        self.size += 1
        if self.head is None:
            self.head = Node(data)
        else:
            p = Node(data)
            p.next = self.head
            self.head.previous = p
            self.head = p

    def remove(self, index):
        if self.head is None:
            raise ValueError('Removing off an empty list')
        if index < 0 or index >= self.size:
            raise IndexError("Index is either negative or greater than the list size.")
        current = self.head
        if index == 0:
            self.head = self.head.next
            self.head.previous = None
        else:
            for _ in range(index -1):
                current = current.next
            p = current.next.next
            if p is None:
                current.next = None
            else:
                current.next = p
                p.previous = current

    def __sizeof__(self):
        return self.size

    def __repr__(self):
        res = '[ '
        current = self.head
        while current is not None:
            res += str(current.data)
            res += ' '
            current = current.next
        res += ']'
        return res


class Node:
    def __init__(self, data):
        if data is None:
            raise ValueError('Node value cannot be None')
        self.data = data
        self.previous = None
        self.next = None

