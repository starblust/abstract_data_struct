#two - direction queue

class Deque:
    def __init__(self):
        self.d = []

    def isEmpty(self):
        return self.d == []

    def addFront(self, item):
        self.d.append(item)

    def addRear(self, item):
        self.d.insert(0, item)

    def removeFroant(self):
        if (self.isEmpty()):
            return None
        return self.d.pop()

    def removeRear(self):
        if (self.isEmpty()):
            return None
        return self.d.pop(0)

    def size(self):
        return len(self.d)