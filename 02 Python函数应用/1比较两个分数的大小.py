def compare(a, b, c, d):
    # 交叉相乘
    t1 = a * d
    t2 = b * c

    # 比较两个分数
    if t1 > t2:
        return f"{a}/{b} > {c}/{d}"
    elif t1 < t2:
        return f"{a}/{b} < {c}/{d}"
    else:
        return f"{a}/{b} == {c}/{d}"


# 比较分数 3/4 和 5/6
result = compare(3, 4, 5, 6)
print(result)
