def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix


def get_matrix_from_input():
    rows = int(input("Введите количество строк матрицы: "))
    cols = int(input("Введите количество столбцов матрицы: "))

    matrix = []
    print("Введите элементы матрицы построчно (через пробел):")
    for i in range(rows):
        row_str = input(f"Строка {i+1}: ")
        row_elements = [int(x) for x in row_str.split()]
        if len(row_elements) != cols:
            raise ValueError("Неверное количество элементов в строке.")
        matrix.append(row_elements)

    return matrix


if __name__ == "__main__":
    try:
        matrix = get_matrix_from_input()
        transposed = transpose_matrix(matrix)

        print("\nИсходная матрица:")
        for row in matrix:
            print(row)

        print("\nТранспонированная матрица:")
        for row in transposed:
            print(row)

    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
