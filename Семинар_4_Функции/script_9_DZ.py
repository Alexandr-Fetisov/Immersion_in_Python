"""Задание №9 Напишите функцию для транспонирования матрицы"""

def transpose_matrix(matrix):
    return map(lambda x: list(x), zip(*mat))


mat = [[3, 2, 3], [4, 5, 68], [57, 88, 9], [120, 111, 12]]

print("Your matrix: ")
for i in mat:
    print(i)

new_mat = transpose_matrix(mat)

print("Your new matrix: ")
for i in new_mat:
    print(i)