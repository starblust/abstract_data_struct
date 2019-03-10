# FIFO - first in first out

class Queue:
    def __init__(self):
        self.q = []

    def isEmpty(self):
        return self.q == []

    def enqueue(self, item):
        self.q.insert(0, item)

    def dequeue(self):
        if (self.isEmpty()):
            return None
        return self.q.pop()

    def size(self):
        return len(self.q)