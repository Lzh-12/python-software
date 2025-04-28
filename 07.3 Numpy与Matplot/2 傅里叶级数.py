import numpy  # pip install numpy
import matplotlib.pyplot # pip install matplotlib


def main():
    t = numpy.linspace(-numpy.pi, numpy.pi, 201)
    k = numpy.arange(1, 99)
    k = 2 * k - 1
    f = numpy.zeros_like(t)
    for i in range(len(t)):
        f[i] = numpy.sum(numpy.sin(k * t[i]) / k)
    f = (4 / numpy.pi) * f
    matplotlib.pyplot.plot(t, f)
    matplotlib.pyplot.show()


if __name__ == '__main__':
    main()
    