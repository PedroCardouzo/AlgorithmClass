import sys
from util import timeit
sys.setrecursionlimit(10000)

if __name__ == '__main__':
    from algorithms.is_prime_number import *

    test_cases = [(30, False), (1, False), (4, False), (9, False), (16, False), (25, False), (36, False), (49, False),
                  (64, False), (81, False), (100, False), (121, False), (144, False), (169, False), (196, False),
                  (225, False), (256, False), (289, False), (324, False), (361, False), (400, False), (441, False),
                  (484, False), (529, False), (576, False), (625, False), (676, False), (729, False), (784, False),
                  (841, False), (907, True)]
    l = [a for a, _ in test_cases]*1000
    timeit(lambda: [is_prime_standard(el) for el in l])
    timeit(lambda: [is_prime(el) for el in l])
    print("Tree stuff")
    from algorithms.Tree import test
    test()
