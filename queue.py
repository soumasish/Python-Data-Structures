class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, item):
        p = Node(item)
        if self.head is None:
            self.head = p
            self.tail = p
        else:
            self.tail.next = p
            self.tail = p
        self.size += 1

    def pop(self):
        if self.head is None:
            raise ValueError('Popping off an empty queue.')
        self.head = self.head.next
        self.size -= 1

    def peek(self):
        return self.head.data

    def is_empty(self):
        return self.head is None

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def __repr__(self):
        return "[{}]".format(", ".join(map(str, self)))


class Node:
    def __init__(self, data):
        if data is None:
            raise ValueError('Cannot create None node')
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)
