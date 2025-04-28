import numpy  # pip install numpy


def main():
    types = numpy.dtype([('name', numpy.str_, 50),
                         ('author', numpy.str_, 30),
                         ('item', numpy.int32),
                         ('price', numpy.float32)])
    books = numpy.array([('Java程序设计开发实战', '李兴华', 1, 7980),
                         ('Python开发实战', '李兴华', 2, 8980),
                         ('MySQL开发实战', '李兴华', 2, 9980),
                         ('Spring开发实战', '李兴华', 1, 8980) ], dtype=types)
    print(books)


if __name__ == '__main__':
    main()


