
my_list = []

n = int(input("请输入数据的个数："))

for i in range(n):
    m = int(input("请输入："))
    my_list.append(m)

for i in range(n):
    min = i
    for j in range(i + 1, n):
        if my_list[j] < my_list[min]:
            min = j
    my_list[i], my_list[min] = my_list[min], my_list[i]

print(f"选择排序后的结果：{my_list}")
