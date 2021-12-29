from icecream import ic
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        x=self.items[0]
        del self.items[0]
        return x

    def size(self):
        return len(self.items)


q = Queue()
ic(q.isEmpty())

q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)

ic(q.size())
ic(q.isEmpty())

q.enqueue(8.4)

ic(q.dequeue())
ic(q.dequeue())

ic(q.size())