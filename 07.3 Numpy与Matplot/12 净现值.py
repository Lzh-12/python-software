import numpy  # pip install numpy
import numpy_financial  # pip install numpy-financial
import matplotlib.pyplot  # pip install matplotlib


def main():
    cashflows = numpy.random.randint(100, size=5)
    cashflows = numpy.insert(cashflows, 0, -100)
    print('现金流', cashflows)
    fvals = []
    for i in range(1, 10):  # 使用range函数替换xrange
        fvals.append(numpy_financial.npv(0.03, cashflows))
    matplotlib.pyplot.plot(fvals, 'bo')
    matplotlib.pyplot.show()


if __name__ == '__main__':
    main()
    