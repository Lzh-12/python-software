import numpy  # pip install numpy
import matplotlib.pyplot # pip install matplotlib


def main():
    a = float(9)
    b = float(8)
    t = numpy.linspace(-numpy.pi, numpy.pi, 201)
    x = numpy.sin(a * t + numpy.pi / 2)
    y = numpy.sin(b * t)
    matplotlib.pyplot.plot(x, y)
    matplotlib.pyplot.show()


if __name__ == '__main__':
    main()
