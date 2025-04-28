import numpy  # pip install numpy


def main():
    array_a = numpy.arange(9).reshape(3, 3)
    array_b = 2 * array_a
    print('【水平组合】%s' % numpy.hstack((array_a, array_b)))
    print('【水平组合】%s' % numpy.concatenate((array_a, array_b), axis=1)) # axis为组合方向
    print('【垂直组合】%s' % numpy.vstack((array_a, array_b)))
    print('【垂直组合】%s' % numpy.concatenate((array_a, array_b), axis=0))  # axis为组合方向
    # 深度组合，就是将一系列数组沿着纵轴（深度）方向进行层叠组合。举个例子，有若干张二维平
    # 面内的图像点阵数据，我们可以将这些图像数据沿纵轴方向层叠在一起
    print('【深度组合】%s' % numpy.dstack((array_a, array_b)))
    print('【列组合】%s' % numpy.column_stack((array_a, array_b)))
    print('【行组合】%s' % numpy.row_stack((array_a, array_b)))


if __name__ == '__main__':
    main()
