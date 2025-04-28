import numpy  # pip install numpy


def main():
    array = numpy.arange(-4, 4)
    # remainder函数逐个返回两个数组中元素相除后的余数。如果第二个数字为0，则直接返回0：
    print('【模运算】%s' % numpy.remainder(array, 2))
    print('【模运算】%s' % numpy.mod(array, 2))
    #  fmod函数处理负数的方式与remainder、mod和%不同。所得余数的正负由被除数决定，与除数的正负无关：
    print('【模运算】%s' % numpy.fmod(array, 2))
    print('【模运算】%s' % str(array % 2))


if __name__ == '__main__':
    main()
