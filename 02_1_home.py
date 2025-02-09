# ✅ Стек (Stack) — это структура данных, работающая по принципу "последний пришел, первый ушел"
# (Last In, First Out, LIFO).
#Основные операции со стеком:
#push — добавление элемента в стек,
#pop — удаление верхнего элемента,
#peek — получение верхнего элемента без удаления,
#is_empty — проверка, пуст ли стек.



class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


stack = Stack() # Создаем объекта класса

stack.push(30)
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(111111)

print("Реализация механизма СТЭК")
print(stack.is_empty())
print(stack.size())
print(stack.peek())




