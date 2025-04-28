candies = [10, 2, 8, 22, 16, 4, 10, 6, 14, 20]
count = 0

while len(set(candies)) != 1:
    candies[0] //= 2
    t = candies[0]
    for i in range(1, 10):
        candies[i % len(candies)] //= 2
        candies[i % len(candies)] += t
        t = candies[i % len(candies)] - t
        if candies[i % len(candies)] % 2 == 1:
            candies[i % len(candies)] += 1

    candies[0] += t
    if candies[0] % 2 == 1:
        candies[0] += 1
    count += 1


print(f"经过{count}次后，每个小孩手中的糖一样多，每人有{candies[0]}块糖。")
