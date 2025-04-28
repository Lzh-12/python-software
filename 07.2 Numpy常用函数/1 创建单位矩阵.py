import numpy  # pip install numpy


def main():
    array = numpy.eye(5)
    print('【原始数组】%s' % array)
    numpy.savetxt('yootk_eye_array.txt', array)


if __name__ == '__main__':
    main()
    