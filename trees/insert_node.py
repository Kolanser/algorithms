"""
https://contest.yandex.ru/contest/26207/problems/J/
Добавь узел

Дано BST. Надо вставить узел с заданным ключом. Ключи в дереве могут повторяться.
На вход функции подаётся корень корректного бинарного дерева поиска и ключ,
который надо вставить в дерево. Осуществите вставку этого ключа.
Если ключ уже есть в дереве, то его дубликаты уходят в правого сына.
Таким образом вид дерева после вставки определяется однозначно.
Функция должна вернуть корень дерева после вставки вершины.
Ваше решение должно работать за 
O(h), где h –— высота дерева.

Формат ввода
Ключи дерева – натуральные числа.
"""


LOCAL = True

if not LOCAL:
    from node import Node

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value


def insert(root, key):
    if key < root.value:
        if not root.left:
            root.left = Node(value=key)
        else:
            insert(root.left, key)
    else:
        if not root.right:
            root.right = Node(value=key)
        else:
            insert(root.right, key)
    return root


def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6


if __name__ == '__main__':
    test()