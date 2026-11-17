import numpy as np


def main():
    # 1. Создание векторов и матриц
    hours = np.arange(0, 22, 3)
    line = np.linspace(0, 1, 5)
    zeros = np.zeros(6, dtype=int)
    unknown_table = np.full((2, 3), -1)
    identity = np.eye(3)

    print(hours)
    print(hours.shape, hours.ndim, hours.size, hours.dtype)

    # 2. Индексы и срезы в векторе
    print(hours[2])
    print(hours[-1])
    print(hours[2:6])
    print(hours[::2])
    print(hours[::-1])

    # 3. Строки и столбцы таблицы
    temperatures = np.array([
        [12, 14, 13, 15],
        [11, 13, 16, 17],
        [10, 12, 15, 18],
    ])
    print(temperatures.shape, temperatures.ndim, temperatures.size)
    print(temperatures[1, 2])
    print(temperatures[0])
    print(temperatures[:, -1])
    print(temperatures[:2, 1:])
    center = temperatures[:2, 1:3]
    print(center)
    print(center.shape)


if __name__ == "__main__":
    main()
