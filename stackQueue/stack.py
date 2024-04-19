class Stack:
    def __init__(self, maxSize = 200):
        self.data = []
        self.maxSize = maxSize

    def isFull(self):
        if len(self.data) >= self.maxSize:
            return True
        return False

    def push(self, sth):
        if self.isFull():
            print("stack full")
            return
        self.data.append(sth)

    def isEmpty(self):
        if len(self.data) == 0:
            return True
        return False

    def pop(self):
        if self.isEmpty():
            print("it's empty")
            return
        return self.data.pop()

stack = Stack()
stack.push("hello")
he = stack.pop()
print(he)
stack.pop()
stack.pop()