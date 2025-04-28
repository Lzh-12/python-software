import numpy  # pip install numpy


def main():
    array = numpy.arange(9)
    print('【最大值】%s' % numpy.max(array))
    print('【最小值】%s' % numpy.min(array))
    print('【大小差】%s' % numpy.ptp(array))


if __name__ == '__main__':
    main()
    