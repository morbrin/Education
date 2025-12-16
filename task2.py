def input_matrix(rows, cols, matrix_name):
    """
    Функция для ввода матрицы с клавиатуры
    """
    print(f"\nВведите элементы матрицы {matrix_name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                try:
                    element = float(input(f"Элемент [{i + 1}][{j + 1}]: "))
                    row.append(element)
                    break
                except ValueError:
                    print("Ошибка! Введите число.")
        matrix.append(row)
    return matrix


def print_matrix(matrix, name):
    """
    Функция для красивого вывода матрицы
    """
    print(f"\n{name}:")
    for row in matrix:
        print("[" + " ".join(f"{elem:8.2f}" for elem in row) + "]")


def matrix_multiply(matrix1, matrix2):
    """
    Функция для умножения двух матриц
    """
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    # Проверка возможности умножения
    if cols1 != rows2:
        raise ValueError(
            "Ошибка: Умножение невозможно! Количество столбцов первой матрицы должно равняться количеству строк второй матрицы.")

    # Создание результирующей матрицы, заполненной нулями
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    # Умножение матриц
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


def main():
    """
    Основная функция программы
    """
    print("=" * 50)
    print("       ПРОГРАММА УМНОЖЕНИЯ МАТРИЦ")
    print("=" * 50)

    try:
        # Ввод размеров первой матрицы
        rows1 = int(input("Введите количество строк первой матрицы: "))
        cols1 = int(input("Введите количество столбцов первой матрицы: "))

        # Ввод размеров второй матрицы
        rows2 = int(input("Введите количество строк второй матрицы: "))
        cols2 = int(input("Введите количество столбцов второй матрицы: "))

        # Проверка возможности умножения
        if cols1 != rows2:
            print("\n❌ Ошибка: Умножение невозможно!")
            print("   Количество столбцов первой матрицы должно равняться количеству строк второй матрицы.")
            print(f"   У вас: {cols1} ≠ {rows2}")
            return

        # Ввод матриц
        matrix_a = input_matrix(rows1, cols1, "A")
        matrix_b = input_matrix(rows2, cols2, "B")

        # Вывод введенных матриц
        print_matrix(matrix_a, "Матрица A")
        print_matrix(matrix_b, "Матрица B")

        # Умножение матриц
        result_matrix = matrix_multiply(matrix_a, matrix_b)

        # Вывод результата
        print_matrix(result_matrix, "Результат умножения A × B")

        print("\n✅ Умножение выполнено успешно!")

    except ValueError as e:
        print(f"\n❌ Ошибка ввода: {e}")
    except Exception as e:
        print(f"\n❌ Произошла ошибка: {e}")


def example_with_predefined_matrices():
    """
    Пример работы программы с заранее заданными матрицами
    """
    print("\n" + "=" * 50)
    print("       ПРИМЕР С ЗАРАНЕЕ ЗАДАННЫМИ МАТРИЦАМИ")
    print("=" * 50)

    # Пример матриц
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    B = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]

    print_matrix(A, "Матрица A")
    print_matrix(B, "Матрица B")

    try:
        result = matrix_multiply(A, B)
        print_matrix(result, "Результат A × B")
    except ValueError as e:
        print(f"❌ {e}")


if __name__ == "__main__":
    # Запуск основного режима с вводом с клавиатуры
    main()

    # Демонстрация примера с заранее заданными матрицами
    example_with_predefined_matrices()