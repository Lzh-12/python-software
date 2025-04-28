num = []

for i in range(4):
    n = float(input("请输入邮票的面值："))
    num.append(n)

num = sorted(num, reverse=True)

print(f"最大值：{num[0] * 3 + num[1] + num[2]}")
