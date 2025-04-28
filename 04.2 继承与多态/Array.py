# 整型数组的操作类
class IntArray:
    def __init__(self, size):
        self.array = [0] * size
        self.index = 0

    # 添加数据
    def add(self, data):
        if self.index < len(self.array):
            self.array[self.index] = data
            self.index += 1
        else:
            print(f"超过数组长度，需要扩容")

    # 取得数组中的全部数据
    def get(self):
        return self.array

    # 扩充指定的容量
    def extend(self, add_size):
        self.array.extend([0] * add_size)


# 排序类
class SortedArray(IntArray):
    def __init__(self, size):
        super().__init__(size)

    # 取得排序出来的结果
    def get(self):
        return sorted(super().get())


# 反转类
class ReversedArray(IntArray):
    def __init__(self, size):
        super().__init__(size)

    # 取得反转出来的结果
    def get(self):
        return super().get()[::-1]


if __name__ == "__main__":
    # 创建IntArray对象
    array = IntArray(2)
    array.add(10)
    array.add(5)
    print("Original Array:", array.get())
    array.extend(3)
    print("Extend Array:", array.get())

    sort_array = SortedArray(3)
    sort_array.add(3)
    sort_array.add(2)
    sort_array.add(1)
    print("Sorted Array:", sort_array.get())

    reverse_array = ReversedArray(5)
    reverse_array.add(1)
    reverse_array.add(2)
    reverse_array.add(3)
    reverse_array.add(8)
    reverse_array.add(9)
    print("Reversed Array:", reverse_array.get())
