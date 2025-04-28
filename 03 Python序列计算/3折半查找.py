lt = [1, 2, 3, 4, 5, 6, 7, 8, 9]

m = int(input("请输入一个整数："))
l = 0
r = len(lt) - 1

while l <= r:
    mid = (l + r) // 2
    if lt[mid] == m:
        print("找到，下标为：", mid)
        exit()
    if lt[mid] < m:
        l = mid + 1
    elif lt[mid] > m:
        r = mid - 1

print(f"数据未发现！")
