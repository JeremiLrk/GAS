class QueueItemType:
    def __init__(self, data):
        self.data = data
        self.next = None
class MyQueue:
    def __init__(self):
        self.front = None
        self.back = None

    def isEmpty(self):
        return self.front is None

    def enqueue(self, newItem):
        new_node = QueueItemType(newItem)
        if self.isEmpty():
            self.front = self.back = new_node
        else:
            new_node.next = self.front
            self.front = new_node
        return True

    def dequeue(self):
        if self.isEmpty():
            return (None, False)
        else:
            current = self.front
            if current.next is None:  # Only one element in the queue
                removed_item = current.data
                self.front = self.back = None
                return (removed_item, True)
            while current.next != self.back:
                current = current.next
            removed_item = self.back.data
            self.back = current
            self.back.next = None
            return (removed_item, True)

    def getFront(self):
        if self.isEmpty():
            return (None, False)
        else:
            return (self.back.data, True)

    def save(self):
        elements = []
        current = self.front
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def load(self, items):
        self.front = None
        self.back = None
        for item in reversed(items):
            self.enqueue(item)



if __name__ == "__main__":
    q = MyQueue()
    print(q.isEmpty())
    print(q.getFront()[1])
    print(q.dequeue()[1])
    print(q.enqueue(2))
    print(q.enqueue(4))
    print(q.isEmpty())
    print(q.dequeue()[0])
    q.enqueue(5)
    print(q.save())

    q.load(['a', 'b', 'c'])
    print(q.save())
    print(q.dequeue()[0])
    print(q.save())
    print(q.getFront()[0])
    print(q.save())