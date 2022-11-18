"""
https://contest.yandex.ru/contest/26207/problems/A/
Лампочки

Гоша повесил на стену гирлянду в виде бинарного дерева, в узлах которого находятся лампочки.
У каждой лампочки есть своя яркость. Уровень яркости лампочки соответствует числу, расположенному в узле дерева.
Помогите Гоше найти самую яркую лампочку в гирлянде, то есть такую, у которой яркость наибольшая.
https://contest.yandex.ru/testsys/statement-image?imageId=4fb8ce32e82f20ff3923b6bdf4821e5af4df6fa21eaa49f99e8b330bb3a6d757
Формат ввода
На вход подается корень дерева.

Формат вывода
Функция должна вернуть максимальное значение яркости в узле дерева.
"""

LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root):
    def get_max_value(node, max_value_previous):
        max_value = max_value_previous
        if node.value > max_value_previous:
            max_value = node.value
        if node.left:
            max_value = get_max_value(node.left, max_value)
        if node.right:
            max_value = get_max_value(node.right, max_value)
        return max_value
    return get_max_value(root, root.value)


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


if __name__ == '__main__':
    test()
