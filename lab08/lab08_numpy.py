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

    # 4. Прямоугольные срезы
    matrix = np.arange(1, 26).reshape(5, 5)
    first_rows = matrix[:3, :]
    print(first_rows)
    print(first_rows.shape)
    last_rows = matrix[-2:, :]
    print(last_rows)
    print(last_rows.shape)
    first_columns = matrix[:, :2]
    print(first_columns)
    print(first_columns.shape)
    fragment = matrix[1:4, 2:5]
    print(fragment)
    print(fragment.shape)
    corner = matrix[-2:, -2:]
    print(corner)
    print(corner.shape)

    # 5. Изменение массива с помощью срезов
    vector = np.array([10, 20, 30, 40, 50])
    vector[1:4] = 0

    small_matrix = np.arange(1, 10).reshape(3, 3)
    small_matrix[0, :] = -1
    small_matrix[1:, 1:] = 9

    # copy() создаёт независимый массив, поэтому исходные данные сохраняются.
    changed_hours = hours.copy()
    changed_hours[2:5] = 99
    changed_hours[::2] = -1
    print(changed_hours)
    print(hours)

    changed_matrix = matrix.copy()
    changed_matrix[1, :] = 0
    changed_matrix[:, -1] = -1
    changed_matrix[1:4, 1:4] = 100
    print(changed_matrix)
    print(matrix)

    # 6. Изменение формы
    # reshape(3, 4) сохраняет 12 элементов, а для reshape(5, 3) нужно 15.
    numbers = np.arange(12)
    table = numbers.reshape(3, 4)
    transposed = table.T
    print(numbers.shape)
    print(table.shape)
    print(transposed.shape)


if __name__ == "__main__":
    main()
