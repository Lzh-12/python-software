import numpy  # pip install numpy


def main():
    array1 = numpy.arange(9)  # 一维数组
    print('【数组切片】%s' % array1[3:7])
    array2 = numpy.arange(24).reshape(2, 3, 4)  # 三维数组
    # 访问三维数组 array2 中索引为 (0, 0, 0) 的元素，即第一个二维数组的第一行的第一个元素。
    print('【数组切片】%s' % array2[0, 0, 0])
    # 访问三维数组 array2 中所有二维数组的第一行的第一个元素，即第一个维度上的所有二维数组的第一行的第一个元素。
    print('【数组切片】%s' % array2[:, 0, 0])
    # 访问三维数组 array2 中第一个二维数组的所有行的第一个元素，即第一个二维数组中每一行的第一个元素。
    print('【数组切片】%s' % array2[0, :, 0])
    # 访问三维数组 array2 中第一个二维数组的第一行的所有元素，即第一个二维数组中第一行的所有元素。
    print('【数组切片】%s' % array2[0, 0, :])


if __name__ == '__main__':
    main()
