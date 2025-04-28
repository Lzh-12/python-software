import numpy  # pip install numpy
import matplotlib.pyplot # pip install matplotlib


def main():
    N = 10000
    lognormal_values = numpy.random.lognormal(size=N)
    dummy, bins, dummy = matplotlib.pyplot.hist(lognormal_values, int(numpy.sqrt(N)), density=True, lw=1)
    sigma = 1
    mu = 0
    x = numpy.linspace(min(bins), max(bins), len(bins))
    pdf = numpy.exp(-(numpy.log(x) - mu) ** 2 / (2 * sigma ** 2)) / (x * sigma * numpy.sqrt(2 * numpy.pi))
    matplotlib.pyplot.plot(x, pdf, lw=3)
    matplotlib.pyplot.show()


if __name__ == '__main__':
    main()
    