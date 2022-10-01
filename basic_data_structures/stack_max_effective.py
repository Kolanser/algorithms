"""
Стек - MaxEffective
Реализуйте класс StackMaxEffective, поддерживающий операцию определения
максимума среди элементов в стеке. Сложность операции должна быть O(1).
Для пустого стека операция должна возвращать None. При этом push(x) и
pop() также должны выполняться за константное время.

Формат ввода
В первой строке записано одно число — количество команд, оно не превосходит
100000. Далее идут команды по одной в строке. Команды могут быть
следующих видов:
push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max нужно напечатать «None»,
для команды pop — «error».
Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения.
Если стек пустой, для команды get_max() напечатайте «None».
Если происходит удаление из пустого стека — напечатайте «error».

Пример 1
Ввод
10
pop
pop
push 4
push -5
push 7
pop
pop
get_max
pop
get_max
Вывод
error
error
4
None
Пример 2
Ввод
10
get_max
push -6
pop
pop
get_max
push 2
get_max
pop
push -2
push -6
Вывод
None
error
None
2
"""


class StackEmptyPop(Exception):
    """Стек пуст для извлечения крайнего элемента."""

    pass


class StackEmptyMax(Exception):
    """Стек пуст для извлечения максимального элемента."""

    pass


class StackMaxEffective:

    def __init__(self):
        self.__items = []
        self.__max_elements = []
        self.__size = 0

    def push(self, item):
        item = int(item)
        self.__items.append(item)
        self.__size += 1
        if self.__size == 1 or item >= self.__max_elements[-1]:
            self.__max_elements.append(item)

    def pop(self):
        if not self.__size:
            raise StackEmptyPop
        if self.__max_elements[-1] == self.__items[-1]:
            self.__max_elements.pop()
        self.__items.pop()
        self.__size -= 1

    def get_max(self):
        if not self.__size:
            raise StackEmptyMax
        return str(self.__max_elements[-1])


def read_input():
    n = int(input())
    commands = [input() for _ in range(n)]
    return commands


def execute_commands(stack, commands):
    for command in commands:
        try:
            command, *args = command.split()
            result = getattr(stack, command)(*args)
            if result:
                print(result)
        except StackEmptyPop:
            print('error')
        except StackEmptyMax:
            print('None')


def main():
    stack = StackMaxEffective()
    commands = read_input()
    execute_commands(stack, commands)


if __name__ == '__main__':
    main()
