import numpy  # pip install numpy
import matplotlib.pyplot  # pip install matplotlib


def main():
    points = numpy.zeros(100)
    outcomes = numpy.random.hypergeometric(25, 1, 3, size=len(points))
    for i in range(len(points)):
        if outcomes[i] == 3:
            points[i] = points[i - 1] + 1
        elif outcomes[i] == 2:
            points[i] = points[i - 1] - 6
        else:
            print(outcomes[i])
    matplotlib.pyplot.plot(numpy.arange(len(points)), points)
    matplotlib.pyplot.show()


if __name__ == '__main__':
    main()
