a, b = map(int, input().split())

# 6 3
m = max(a, b)
n = min(a, b)

t = m % n
while t != 0:
    m = n
    n = t
print(f"最大公约数是{n}")
