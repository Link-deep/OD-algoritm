#✅ Бинарное дерево — это вид дерева, в котором каждый узел имеет не более двух потомков.


class Node():

    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.value == key:
            return root
        elif root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


root = Node(70)

root = insert(root, 50)
root = insert(root, 90)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 60)
root = insert(root, 80)

