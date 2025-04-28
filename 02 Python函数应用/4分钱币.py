def func(num, sum):
    if num < 1:
        return sum
    else:
        if sum % 4 != 0:
            return 0
        else:
            sum = sum / 4 * 5 + 1
            return func(num - 1, sum)


fisher = ['E', 'D', 'C', 'B', 'A']

for i in range(4, 10000):
    res = int(func(5, i))
    if res:
        print(f"至少合伙捕到{res}条鱼")
        for j in range(5):
            i = int(i // 4 * 5 + 1)
            print(f"{fisher[j]}醒来后看到{i}条鱼")
        break


