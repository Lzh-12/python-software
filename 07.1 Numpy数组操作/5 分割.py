import numpy  # pip install numpy


def main():
    array = numpy.arange(9).reshape(3, 3)
    print('【水平分割】%s' % numpy.hsplit(array, 3))
    print('【垂直分割】%s' % numpy.vsplit(array, 3))
    array = numpy.arange(27).reshape(3, 3, 3)
    print('【深度分割】%s' % numpy.dsplit(array, 3))


if __name__ == '__main__':
    main()
