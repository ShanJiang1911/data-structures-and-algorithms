class PseudoQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):

        while len(self.stack1) != 0:
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()

        self.stack1.append(x)

        while len(self.stack2) != 0:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()

    def dequeue(self):

        if len(self.stack1) == 0:
            print("Queue is Empty")

        x = self.stack1[-1]
        self.stack1.pop()
        return x

if __name__ == '__main__':
    q = PseudoQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
