class Hashmap:
    def __init__(self):
        self.store = [] * 16

    def get(self, key):
        index = hash(key)
        current = self.store[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next

    def put(self, key, value):
        index = hash(key)/16
        p = Node(key, value)
        if self.store[index] is None:
            self.store[index] = p
        else:
            p.next = self.store[index]
            self.store[index] = p


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None