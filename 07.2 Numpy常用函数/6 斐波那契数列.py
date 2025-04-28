import numpy  # pip install numpy


def main():
    array = numpy.matrix([[1, 1], [1, 0]])
    # 计算斐波那契数列中的第8个数，即矩阵的幂为8减去1。计算出的斐波那契数位于矩阵的对角线上
    print('【斐波那契数列】计算斐波那契数列中的第8个数：%s' % (array ** 7)[0, 0])
    # 利用黄金分割公式或通常所说的比奈公式（Binet’ s Formula），加上取整函数，就可以直接计算斐波那契数。
    array = numpy.arange(1, 9)
    sqrt5 = numpy.sqrt(5)
    phi = (1 + sqrt5) / 2
    fibonacci = numpy.rint((phi ** array - (-1 / phi) ** array) / sqrt5)
    print('【斐波那契数列】计算前8个斐波那契数：%s' % fibonacci)


if __name__ == '__main__':
    main()
