import numpy  # pip install numpy


def main():
    array_a = numpy.array([2, 6, 5])
    array_b = numpy.array([1, 2, 3])
    print('【除法计算】%s' % numpy.divide(array_a, array_b))
    # true_divide函数与数学中的除法定义更为接近，即返回除法的浮点数结果而不作截断
    print('【除法计算】%s' % numpy.true_divide(array_a, array_b))
    # floor_divide函数总是返回整数结果，相当于先调用divide函数再调用floor函数
    print('【除法计算】%s' % numpy.floor_divide(array_a, array_b))
    print('【除法计算】%s' % str(array_a / array_b))
    print('【除法计算】%s' % str(array_a // array_b))


if __name__ == '__main__':
    main()
    