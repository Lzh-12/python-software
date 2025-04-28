import numpy  # pip install numpy
import numpy_financial  # pip install numpy-financial
import matplotlib.pyplot  # pip install matplotlib


def main():
    print('未来收益', numpy_financial.fv(0.03 / 4, 5 * 4, -10, -1000))
    fvals = []
    for i in range(1, 10):  # 使用range函数替换xrange
        fvals.append(numpy_financial.fv(0.03 / 4, i * 4, -10, -1000))
    matplotlib.pyplot.plot(fvals, 'bo')
    matplotlib.pyplot.show()


if __name__ == '__main__':
    main()
