"""
https://contest.yandex.ru/contest/26207/problems/K/
Выведи диапазон

Напишите функцию, которая будет выводить по неубыванию все ключи от L до 
R включительно в заданном бинарном дереве поиска.
Ключи в дереве могут повторяться. Решение должно иметь сложность 
O(h+k), где h –— глубина дерева, k — число элементов в ответе.
В данной задаче если в узле содержится ключ 
x, то другие ключи, равные x, могут быть как в правом, так и в левом поддереве данного узла.
(Дерево строил стажёр, так что ничего страшного).

Формат ввода
На вход функции подаётся корень дерева и искомый ключ.
Ключи – натуральные числа. Гарантируется, что L≤R.
В итоговом решении не надо определять свою структуру / свой класс, описывающий вершину дерева.

Формат вывода
Функция должна напечатать по неубыванию все ключи от L до R по одному в строке.
"""


LOCAL = True

if LOCAL:
    class Node:  
        def __init__(self, left=None, right=None, value=0):  
            self.right = right
            self.left = left
            self.value = value


def print_range(node, l, r):
    if node.left and node.value >= l:
        print_range(node.left, l, r)
    if l <= node.value <= r:
        print(node.value)
    if node.right and node.value <= r:
        print_range(node.right, l, r)


def test():
    node1 = Node(None, None, 2)
    node2 = Node(None, node1, 1)
    node3 = Node(None, None, 8)
    node4 = Node(None, node3, 8)
    node5 = Node(node4, None, 9)
    node6 = Node(node5, None, 10)
    node7 = Node(node2, node6, 5)
    print_range(node7, 2, 8) 
    # expected output: 2 5 8 8


if __name__ == '__main__':
    test()
