import numpy  # pip install numpy
import matplotlib.pyplot # pip install matplotlib


def main():
    t = numpy.linspace(-numpy.pi, numpy.pi, 201)
    k = numpy.arange(1, 5)
    f = numpy.zeros_like(t)
    for i in range(len(t)):
        f[i] = numpy.sum(numpy.sin(2 * numpy.pi * k * t[i]) / k)
    f = (-2 / numpy.pi) * f
    matplotlib.pyplot.plot(t, f, lw=1.0)
    matplotlib.pyplot.plot(t, numpy.abs(f), lw=2.0)
    matplotlib.pyplot.show()


if __name__ == '__main__':
    main()
    