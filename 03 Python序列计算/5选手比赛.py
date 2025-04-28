score = [5, 3, 4, 7, 3, 5, 6]

# 转为集合去重
rank = set(sorted(score))

for i in score:
    for index, j in enumerate(rank):
        if i == j:
            print(index + 1)
            break
