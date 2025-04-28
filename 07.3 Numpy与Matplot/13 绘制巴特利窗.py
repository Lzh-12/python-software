import numpy  # pip install numpy
import matplotlib.pyplot  # pip install matplotlib


def main():
    window = numpy.bartlett(42)
    matplotlib.pyplot.plot(window)
    matplotlib.pyplot.show()


if __name__ == '__main__':
    main()
