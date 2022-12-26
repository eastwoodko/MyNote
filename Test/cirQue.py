class CircularQueue:
    def __init__(self, MaxSize=64):
        self.Queue = [None] * MaxSize
        self.head = 0
        self.tail = 0
        self.MaxSize = MaxSize
        self.getPos = 0

    def size(self):
        if self.tail >= self.head:
            return (self.tail - self.head)
        else:
            return (self.MaxSize - (self.head - self.tail))

    def enQueue(self, data):
        if self.size() == self.MaxSize - 1:
            return False
        self.Queue.append(data)
        self.tail = (self.tail + 1) % self.MaxSize

        return True

    def deQueue(self):
        if self.size() == 0:
            return None

        data = self.Queue[self.head]
        self.head = (self.head +1) % self.MaxSize

        return data

    ## getQueue , getNextQueue, getNextQueue, ..... (eoq 까지 자료를 가져오는 방법)
    def getQueue(self):
        if self.size() == 0:
            return None

        self.getPos = self.head
        return self.Queue[self.head]

    def getNextQueue(self):
        self.getPos = (self.getPos + 1) % self.MaxSize
        if self.getPos == self.tail:
            return None
        else:
            return self.Queue[self.getPos]





