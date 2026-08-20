""" Topic 2. Implement Queue using Array or List """

class Queue:
    def __int__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            print("Cannot dequeue, from empty queue")
            return
        x = self.items.pop(0)
        return x

    def front(self):
        if len(self.items) == 0:
            print("Cannot peek, queue is empty")
            return
        return self.items[0]

    def rear(self):
        if len(self.items) == 0:
            print("Cannot read, queue is empty")
            return self.items[-1]

    def size(self):
        return len(self.items)