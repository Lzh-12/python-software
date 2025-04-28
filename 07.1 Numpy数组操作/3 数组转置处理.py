import numpy  # pip install numpy


def main():
    array = numpy.arange(24).reshape(2, 3, 4) # 三维数组
    print('【多维数组】%s' % array)
    print('---' * 30)
    print('【数组展平】%s' % array.ravel())
    print('---' * 30)
    # flatten()函数会请求分配内存来保存结果，而ravel函数只是返回数组的一个视图
    print('【数组展平】%s' % array.flatten())
    print('---' * 30)
    print('【矩阵转置】%s' % array.transpose())
    print('---' * 30)
    print('【矩阵重置】%s' % array.reshape((2, 12)))


if __name__ == '__main__':
    main()
