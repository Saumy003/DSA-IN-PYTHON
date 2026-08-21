""" Topic 5. Implement Queue using Stack """

#st1 --> Stack1
#st2 --> Stack2

class QueueUsingStack:
    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x):
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(x)
        while self.st2:
            self.st1.append(self.st2.pop())

    def pop(self):
        if not self.st1:
            print("Stack is empty")
            return -1
        top_element = self.st1.pop()
        return top_element

    def peek(self):
        if not self.str1:
            print("Stack is empty")
            return -1
        return self.st1[-1]

    def is_empty(self):
        return not self.st1