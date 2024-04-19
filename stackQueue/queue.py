class Queue:
    def __init__(self, maxQueueSize = 200):
        self.data = []
        self.maxQueueSize = maxQueueSize

    def isFullQueue(self):
        if len(self.data) >= self.maxQueueSize:
            return True
        return False

    def addQueue(self, sth):
        if self.isFullQueue() == True:
            print("it's full")
            return
        self.data.append(sth)

    def isEmptyQueue(self):
        if len(self.data) == 0:
            return True
        return False

    def deleteQueue(self):
        if self.isEmptyQueue():
            print("it's empty")
            return
        return self.data.pop(0)

q = Queue()
q.addQueue(1)
q.addQueue(2)
print(q.deleteQueue())