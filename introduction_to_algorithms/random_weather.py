"""
Хаотичность погоды
Метеорологическая служба вашего города решила исследовать
погоду новым способом.

Под температурой воздуха в конкретный день будем понимать
максимальную температуру в этот день.
Под хаотичностью погоды за n дней служба понимает количество дней,
в которые температура строго больше, чем в день до (если такой существует
 и в день после текущего (если такой существует). Например, если за 5
 дней максимальная температура воздуха составляла [1, 2, 5, 4, 8] градусов,
 то хаотичность за этот период равна 2: в 3-й и 5-й дни выполнялись описанные условия.
Определите по ежедневным показаниям температуры хаотичность погоды за этот период.

Заметим, что если число показаний n=1, то единственный день будет хаотичным.

Формат ввода
В первой строке дано число n –— длина периода измерений в днях, 1 ≤ n≤ 105.
Во второй строке даны n целых чисел –— значения температуры в каждый из n дней.
Значения температуры не превосходят 273 по модулю.

Формат вывода
Выведите единственное число — хаотичность за данный период.

Пример 1
Ввод	Вывод
7
-1 -10 -8 0 2 0 5
3
Пример 2
Ввод	Вывод
5
1 2 5 4 8
2
"""


from typing import List


def get_weather_randomness(n: int, temperatures: List[int]) -> int:
    if n == 1:
        return n
    days_weather_randomness = 0
    if temperatures[0] > temperatures[1]:
        days_weather_randomness = days_weather_randomness + 1
    if temperatures[-1] > temperatures[-2]:
        days_weather_randomness = days_weather_randomness + 1
    for i in range(1, n-1):
        if (
            temperatures[i] > temperatures[i-1]
            and temperatures[i] > temperatures[i+1]
        ):
            days_weather_randomness = days_weather_randomness + 1
    return days_weather_randomness


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().split()))
    return n, temperatures


n, temperatures = read_input()
print(get_weather_randomness(n, temperatures))
