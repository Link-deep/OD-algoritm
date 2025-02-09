# ✅Пузырьковая сортировка работает путем многократного прохода по массиву,
# сравнивая соседние элементы и меняя их местами, если они находятся в неправильном порядке.
# Процесс продолжается до тех пор, пока массив не будет отсортирован.


mas = [5, 7, 4, 3, 8, 2]
n = 6

for run in range(n-1):  # ЦИКЛ количества проходов
    for i in range(n - 1 - run): # ЦИКЛ перебирает массив и работает с каждым элементом.
        if mas[i] > mas[i + 1]:
            mas[i], mas[i + 1] = mas[i + 1], mas[i]

print(mas)



# ✅Быстрая сортировка использует метод «разделяй и властвуй».
# Она выбирает опорный элемент (pivot) и разделяет массив на две части:
# элементы меньше опорного и элементы больше опорного.
# Затем сортировка применяется рекурсивно к каждой части.


def quick_sort(s):
    if len(s) <= 1:
        return s
    element = s[0]
    left = list(filter(lambda i: i < element, s))
    center = [i for i in s if i==element]
    right = list(filter(lambda i: i > element, s))

    return quick_sort(left) + center + quick_sort(right)


print(quick_sort([5, 2, 9, 0, 1, 5]))


# Сортировка выбором работает путем поиска минимального элемента в неотсортированной части массива
# и его обмена с первым элементом этой части.
# Затем процесс повторяется для оставшейся части массива.

a = [-3, 5, 0, -8, 1, 10]

def selection_sort(arr):
   for i in range(len(arr)):
       min_index = i
       for j in range(i+1, len(arr)):
           if arr[j] < arr[min_index]:
               min_index = j
       arr[i], arr[min_index] = arr[min_index], arr[i]
   return arr

print(selection_sort(a))

# ЛИБО без return *если не возвращаем
# selection_sort(a)
# print(a)



# ✅Сортировка вставками работает путем последовательного перемещения элементов массива,
# вставляя каждый элемент на его правильное место в уже отсортированной части массива.

ab = [13, 1, 5, 8 ,99, 0, -8, 1, 10]

def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insert_sort(ab))


