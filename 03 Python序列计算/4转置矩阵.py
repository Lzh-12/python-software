array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_array = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(array[0])):
    for j in range(len(array[0])):
        new_array[j][i] = array[i][j]

print(f"转置后的矩阵{new_array}")
