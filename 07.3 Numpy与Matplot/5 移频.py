import numpy  # pip install numpy
import matplotlib.pyplot # pip install matplotlib


def main():
    x = numpy.linspace(0, 2 * numpy.pi, 30)
    wave = numpy.cos(x)
    transformed = numpy.fft.fft(wave)
    shifted = numpy.fft.fftshift(transformed)
    print(numpy.abs(numpy.fft.ifftshift(shifted) - transformed) < 10 ** -9)
    matplotlib.pyplot.plot(transformed, lw=2)
    matplotlib.pyplot.plot(shifted, lw=3)
    matplotlib.pyplot.show()


if __name__ == '__main__':
    main()
    