class Stack:
    def __init__(self):
        self.items = []

    def __init__(self, initial_items=None):
        if initial_items is None:
            self.items = []
        else:
            self.items = list(initial_items)

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)