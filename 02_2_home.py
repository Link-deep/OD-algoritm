# ✅ Очередь (Queue) — это структура данных, работающая по принципу
# "первый пришел — первый ушел" (First In, First Out).
# [7, 3, 5]
# добаляем enqueue1
# [1, 7, 3, 5]
# удаляем dequeeue
# [1, 7, 3]



class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


queue = Queue() # создаем объекта класса

queue.enqueue(1)
queue.enqueue(7)
queue.enqueue(3)
queue.enqueue(5)
print("Реализация механизма ОЧЕРЕДЬ")
print(queue.is_empty())
print(queue.size())
print(queue.items)

print("Удаляем элемент")

print(queue.dequeue())
print(queue.items)

print("Добаляем элемент 19")
queue.enqueue(19)
print(queue.items)

