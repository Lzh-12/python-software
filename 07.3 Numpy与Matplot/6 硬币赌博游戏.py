import numpy  # pip install numpy
import matplotlib.pyplot # pip install matplotlib


def main():
    cash = numpy.zeros(10000)
    cash[0] = 1000
    outcome = numpy.random.binomial(9, 0.5, size=len(cash))
    for i in range(1, len(cash)):
        if outcome[i] < 5:
            cash[i] = cash[i - 1] - 1
        elif outcome[i] < 10:
            cash[i] = cash[i - 1] + 1
        else:
            raise AssertionError("Unexpected outcome " + outcome)
    print(outcome.min(), outcome.max())
    matplotlib.pyplot.plot(numpy.arange(len(cash)), cash)
    matplotlib.pyplot.show()


if __name__ == '__main__':
    main()
    