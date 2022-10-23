"""
https://contest.yandex.ru/contest/26207/problems/B/
Сбалансированное дерево

Гоше очень понравилось слушать рассказ Тимофея про деревья.
Особенно часть про сбалансированные деревья.
Он решил написать функцию, которая определяет, сбалансировано ли дерево.
Дерево считается сбалансированным, если левое и правое поддеревья каждой вершины отличаются по высоте не больше, чем на единицу.

Формат ввода
На вход функции подаётся корень бинарного дерева.

Формат вывода
Функция должна вернуть True, если дерево сбалансировано в соответствии с критерием из условия, иначе - False.
"""


LOCAL = True


if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def depth_tree(root, h=0):
    if not root:
        return h
    h += 1
    h_left = depth_tree(root.left, h)
    h_right = depth_tree(root.right, h)
    return h_left if h_left > h_right else h_right


def solution(root):
    depth_tree_left = depth_tree(root.left)
    depth_tree_right = depth_tree(root.right)
    if abs(depth_tree_left - depth_tree_right) > 1:
        return False
    is_left_subtree = True
    is_right_subtree = True
    if root.left:
        is_left_subtree = solution(root.left)
    if root.right and is_left_subtree:
        is_right_subtree = solution(root.right)
    return is_left_subtree and is_right_subtree


def test():
    # node9 = Node(9)
    # node8 = Node(8)
    # node7 = Node(7)
    # node6 = Node(6)
    # node5 = Node(5)
    # node4 = Node(4, right=node8)
    # node3 = Node(3, node5)
    # node2 = Node(2, right=node4)
    # node1 = Node(1, node3)
    # node0 = Node(0, node1, node2)
    # print(solution(node4))
    node12 = Node(12)
    node11 = Node(11, right=node12)
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10, right=node11)
    node5 = Node(2, node3, node4)
    print(solution(node5))


if __name__ == '__main__':
    test()
