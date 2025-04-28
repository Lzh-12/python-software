sum = 0
i = 1
for i in range(1, 6):
    j = 1
    for j in range(1, 6):
        k = 1
        for k in range(1, 6):
            if i != j and j != k and i != k:
                sum += 1
                print('A:%2d B:%2d C:%2d' % (i, j, k))

print(f"{sum}")

