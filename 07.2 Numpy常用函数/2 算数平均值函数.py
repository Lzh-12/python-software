import numpy  # pip install numpy


def main():
    array = numpy.arange(9).reshape(3, 3)
    print('【平均值】mean = %s' % numpy.mean(array))


if __name__ == '__main__':
    main()

