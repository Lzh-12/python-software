n = int(input("请输入一个数"))

for i in range(1, n + 1):
    if i % 2 == 1 and i % 3 == 2 and i % 5 == 4 and i % 6 == 5 and i % 7 == 0:
        print(f"{i} ")
        