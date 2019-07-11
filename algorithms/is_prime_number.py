from util import assert_result


# is_prime_standard :: int -> bool
# given a number, return true if it is prime
# time complexity XXXX    space complexity YYYY
def is_prime_standard(n):
    raise NotImplementedError


# is_prime :: int -> bool
# given a number, return true if it is prime
# time complexity XXXX    space complexity YYYY
def is_prime(n):
    raise NotImplementedError

def test():
    test_cases = [(30, False), (1, False), (4, False), (9, False), (16, False), (25, False), (36, False), (49, False), (64, False), (81, False), (100, False), (121, False), (144, False), (169, False), (196, False), (225, False), (256, False), (289, False), (324, False), (361, False), (400, False), (441, False), (484, False), (529, False), (576, False), (625, False), (676, False), (729, False), (784, False), (841, False), (907, True)]
    try:
        for n, exp in test_cases:
            assert_result("t1:\n" + str(n), exp, is_prime_standard(n))
            assert_result("t2:\n" + str(n), exp, is_prime(n))
    except NotImplementedError:
        pass