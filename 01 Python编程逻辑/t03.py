def gcd(x, y):
    if x % y == 0:
        return y
    elif x % y == 1:
        return 1
    else:
        gcd(y, x % y)


def lcm(x, y):
    n = gcd(x, y)
    return int((x * y) / n)


print(f"请输入两个整数")
a, b = list(map(int, input().split()))
res = lcm(a, b)
print(f"最小公倍数{res}")
