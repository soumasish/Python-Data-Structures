class MinHeap:
    def __init__(self):
        self.store = []
        self.currIndex = 0
        self.size = 0

    def push(self, item):
        self.store[self.currIndex] = item
        self.currIndex += 1
        child = self.currIndex
        parent = self.currIndex/2

        while self.store[parent] > self.store[child] and parent > 0:
            tmp = self.store[parent]
            self.store[parent] = self.store[child]
            self.store[child] = tmp

            child = parent
            parent = child/2
        self.size += 1

    def pop(self):
        pass

    def __iter__(self):
        for i in range(len(self.store)):
            yield self.store[i]

    def __repr__(self):
        return "[{}]".format(", ".join(map(str, self)))