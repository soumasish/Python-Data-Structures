class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, item):
        p = Node(item)
        if self.top is None:
            self.top = p
        else:
            p.next = self.top
            self.top = p
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise ValueError('Popping off an empty stack.')
        self.top = self.top.next
        self.size -= 1

    def peek(self):
        if self.is_empty():
            raise ValueError('Peeking into an empty stack.')
        return self.top.data

    def is_empty(self):
        return self.top is None

    def __sizeof__(self):
        return self.size

    def __repr__(self):
        stack_str = '[ '
        current = self.top
        while current is not None:
            stack_str += str(current.data)
            stack_str += ' '
            current = current.next

        stack_str += ']'
        return stack_str


class Node:
    def __init__(self, data):
        if data is None:
            raise ValueError('Cannot instantiate node with a None value.')
        self.data = data
        self.next = None
