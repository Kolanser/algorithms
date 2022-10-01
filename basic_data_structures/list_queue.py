"""
Списочная очередь
https://contest.yandex.ru/contest/23758/problems/J/
Любимый вариант очереди Тимофея — очередь, написанная с использованием связного списка.
Помогите ему с реализацией. Очередь должна поддерживать выполнение трёх команд:

get() — вывести элемент, находящийся в голове очереди, и удалить его. Если очередь пуста,
то вывести «error».
put(x) — добавить число x в очередь
size() — вывести текущий размер очереди
Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее 1000.
В каждой из следующих n строк записаны команды по одной строке.

Формат вывода
Выведите ответ на каждый запрос по одному в строке.

Пример 1
Ввод
10
put -34
put -23
get
size
get
size
get
get
put 80
size
Вывод
-34
1
-23
0
error
error
1
Пример 2
Ввод	
6
put -66
put 98
size
size
get
get
Вывод
2
2
-66
98
Пример 3
Ввод	
9
get
size
put 74
get
size
put 90
size
size
size
error
Вывод
0
74
0
1
1
1

Примечания
Все операции должны выполняться за O(1).
"""


class QueueEmpty(Exception):
    """Очередь пуста."""

    pass


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return str(self.value)


class ListQueue:
    def __init__(self):
        self.__head = Node(None)
        self.__tail = Node(None)
        self.__size_queue = 0

    def size(self):
        return self.__size_queue

    def put(self, x):
        if not self.__size_queue:
            self.__head = Node(x)
            self.__head.__next_item = self.__head
            self.__tail = self.__head
        else:
            self.__tail.__next_item = Node(x, self.__head)
            self.__tail = self.__tail.__next_item
        self.__size_queue += 1

    def get(self):
        old_head = self.__head
        if self.__size_queue == 0:
            raise QueueEmpty
        elif self.__size_queue == 1:
            self.__head = Node(None)
            self.__tail = Node(None)
        else:
            self.__head = old_head.__next_item
            self.__tail.__next_item = self.__head
        self.__size_queue -= 1
        return old_head


def read_input():
    size_commands = int(input())
    commands = [input() for _ in range(size_commands)]
    return commands


def print_command(queue, commands):
    for command in commands:
        try:
            command, *args = command.split()
            result = getattr(queue, command)(*args)
            if result is not None:
                print(result)
        except QueueEmpty:
            print('error')


def main():
    list_queue = ListQueue()
    commands = read_input()
    print_command(list_queue, commands)


if __name__ == '__main__':
    main()
