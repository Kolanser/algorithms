"""
https://contest.yandex.ru/contest/26207/problems/E/
Дерево поиска

Гоша понял, что такое дерево поиска, и захотел написать функцию, которая определяет,
является ли заданное дерево деревом поиска. Значения в левом поддереве должны быть строго меньше
в правом —- строго больше значения в узле.
Помогите Гоше с реализацией этого алгоритма.
https://contest.yandex.ru/testsys/statement-image?imageId=ab959396f5887581ee60a3f8697a05a59e59b1e11f27817a59e6b7ff866cb779

Формат ввода
На вход функции подается корень бинарного дерева.

Формат вывода
Функция должна вернуть True, если дерево является деревом поиска, иначе - False.
"""


LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> bool:
    def _solution(root, min, max):
        if not root:
            return True
        if root.value <= min or root.value >= max:
            return False
        return _solution(root.left, min, root.value) and _solution(root.right, root.value, max)
    return _solution(root.left, root.value, root.value) and _solution(root.right, root.value, root.value)


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == '__main__':
    test()
