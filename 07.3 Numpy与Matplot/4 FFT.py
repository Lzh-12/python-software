import numpy  # pip install numpy
import matplotlib.pyplot # pip install matplotlib


def main():
    x = numpy.linspace(0, 2 * numpy.pi, 30)
    wave = numpy.cos(x)
    transformed = numpy.fft.fft(wave)
    print(numpy.all(numpy.abs(numpy.fft.ifft(transformed) - wave) < 10 ** -9))
    matplotlib.pyplot.plot(transformed)
    matplotlib.pyplot.show()


if __name__ == '__main__':
    main()
    