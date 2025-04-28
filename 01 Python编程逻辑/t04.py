sum = 0
max_score = 0
min_score = 100
for i in range(1, 11):
    print('第%d个评委打分：' % i)
    score = int(input())
    if score < 0 or score > 10:
        print('输入有误，请重新输入')
        exit()

    sum += score
    if score > max_score:
        max_score = score

    if score < min_score:
        min_score = score

print('当前平均分：%d' % ((sum - max_score - min_score) // 8))
