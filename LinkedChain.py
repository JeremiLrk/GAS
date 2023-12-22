class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedChain:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def getLength(self):
        if self.isEmpty():
            return 0
        count = 1
        current = self.head
        while current.next != self.head:
            count += 1
            current = current.next
        return count

    def retrieve(self, position):
        if self.isEmpty() or position < 1:
            return None, False
        current = self.head
        for _ in range(position - 1):
            current = current.next
            if current == self.head:
                return None, False
        return current.data, True

    def insert(self, position, data):
        newNode = Node(data)
        if position < 1:
            return False
        if self.isEmpty():
            if position != 1:
                return False
            self.head = newNode
            newNode.next = newNode
            newNode.prev = newNode
            return True
        current = self.head
        for _ in range(position - 1):
            current = current.next
            if current == self.head:
                return False
        newNode.next = current.next
        newNode.prev = current
        current.next.prev = newNode
        current.next = newNode
        if position == 1:
            self.head = newNode
        return True

    def delete(self, position):
        if self.isEmpty() or position < 1 or position > self.getLength():
            return False
        if self.head.next == self.head:
            self.head = None
            return True
        current = self.head
        for _ in range(position - 1):
            current = current.next
        current.prev.next = current.next
        current.next.prev = current.prev
        if position == 1:
            self.head = current.next
        return True

    def save(self):
        if self.isEmpty():
            return []
        result = []
        current = self.head
        while True:
            result.append(current.data)
            current = current.next
            if current == self.head:
                break
        return result

    def load(self, dataList):
        self.head = None
        for data in dataList:
            self.insert(self.getLength() + 1, data)


if __name__ == "__main__":
    l = LinkedChain()
    print(l.isEmpty())
    print(l.getLength())
    print(l.retrieve(4)[1])
    print(l.insert(4, 500))
    print(l.isEmpty())
    print(l.insert(1, 500))
    print(l.retrieve(1)[0])
    print(l.retrieve(1)[1])
    print(l.save())
    print(l.insert(1, 600))
    print(l.save())
    l.load([10, -9, 15])
    l.insert(3, 20)
    print(l.delete(0))
    print(l.save())
    print(l.delete(1))
    print(l.save())
