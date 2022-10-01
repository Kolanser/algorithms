"""
Дек
https://contest.yandex.ru/contest/23759/problems/A/
Гоша реализовал структуру данных Дек, максимальный размер которого определяется заданным числом. Методы push_back(x), push_front(x), pop_back(), pop_front() работали корректно. Но, если в деке было много элементов, программа работала очень долго. Дело в том, что не все операции выполнялись за O(1). Помогите Гоше! Напишите эффективную реализацию.

Внимание: при реализации используйте кольцевой буфер.

Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее 100000. Во второй строке записано число m — максимальный размер дека. Он не превосходит 50000. В следующих n строках записана одна из команд:

push_back(value) – добавить элемент в конец дека. Если в деке уже находится максимальное число элементов, вывести «error».
push_front(value) – добавить элемент в начало дека. Если в деке уже находится максимальное число элементов, вывести «error».
pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то вывести «error».
pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст, то вывести «error».
Value — целое число, по модулю не превосходящее 1000.
Формат вывода
Выведите результат выполнения каждой команды на отдельной строке. Для успешных запросов push_back(x) и push_front(x) ничего выводить не надо.

Пример 1
Ввод	
4
4
push_front 861
push_front -819
pop_back
pop_back
Вывод
861
-819
Пример 2
Ввод	
7
10
push_front -855
push_front 0
pop_back
pop_back
push_back 844
pop_back
push_back 823
Вывод
-855
0
844
Пример 3
Ввод	
6
6
push_front -201
push_back 959
push_back 102
push_front 20
pop_front
pop_back
Вывод
20
102
"""


class DequeEmpty(Exception):
    """Пустой дек."""

    pass


class DequeOverflow(Exception):
    """Дек переполнен."""

    pass


class Deque:
    def __init__(self, max_size):
        self.__deque = [None] * max_size
        self.__max_size = max_size
        self.__head = 0
        self.__tail = 0
        self.__size_deque = 0

    def push_back(self, value):
        if self.__size_deque == self.__max_size:
            raise DequeOverflow
        if self.__size_deque:
            self.__tail = (self.__tail + 1) % self.__max_size
        self.__deque[self.__tail] = value
        self.__size_deque += 1

    def push_front(self, value):
        if self.__size_deque == self.__max_size:
            raise DequeOverflow
        if self.__size_deque:
            self.__head = self.__head - 1
        self.__deque[self.__head] = value
        self.__size_deque += 1

    def pop_front(self):
        if not self.__size_deque:
            raise DequeEmpty
        value = self.__deque[self.__head]
        self.__deque[self.__head] = None
        self.__size_deque -= 1
        if self.__size_deque:
            self.__head = (self.__head + 1) % self.__max_size
        return value

    def pop_back(self):
        if not self.__size_deque:
            raise DequeEmpty
        value = self.__deque[self.__tail]
        self.__deque[self.__tail] = None
        self.__size_deque -= 1
        if self.__size_deque:
            self.__tail -= 1
        return value


def read_input():
    count_commands = int(input())
    max_size_dec = int(input())
    commands = [input() for _ in range(count_commands)]
    return max_size_dec, commands


def print_commands(max_size_dec, commands):
    deque = Deque(max_size_dec)
    for command in commands:
        try:
            command, *args = command.split()
            result = getattr(deque, command)(*args)
            if result:
                print(result)
        except DequeEmpty:
            print('error')
        except DequeOverflow:
            print('error')


def main():
    max_size_dec, commands = read_input()
    print_commands(max_size_dec, commands)


if __name__ == '__main__':
    main()
