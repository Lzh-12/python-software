import numpy  # pip install numpy
import matplotlib.pyplot # pip install matplotlib


def main():
    N = 10000
    normal_values = numpy.random.normal(size=N)
    dummy, bins, dummy = matplotlib.pyplot.hist(normal_values, int(numpy.sqrt(N)), density=True, lw=1)
    sigma = 1
    mu = 0
    matplotlib.pyplot.plot(bins, 1/(sigma * numpy.sqrt(2 * numpy.pi)) *
                           numpy.exp( - (bins -mu)**2 / (2 * sigma**2) ),lw=2)
    matplotlib.pyplot.show()


if __name__ == '__main__':
    main()
