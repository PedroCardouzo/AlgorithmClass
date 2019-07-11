from util import assert_result


# is_prime_standard :: int -> bool
# given a number, return true if it is prime
# time complexity XXXX    space complexity YYYY
def is_prime_standard(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# is_prime :: int -> bool
# given a number, return true if it is prime
# time complexity XXXX    space complexity YYYY
def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    sqrt_n = int(n**0.5+1)  # floating point numbers get +1 then decimal places ignored in int conversion
    for i in range(2, sqrt_n):
        if n % i == 0:
            return False
    return True

def test():
    test_cases = [(30, False), (1, False), (4, False), (9, False), (16, False), (25, False), (36, False), (49, False), (64, False), (81, False), (100, False), (121, False), (144, False), (169, False), (196, False), (225, False), (256, False), (289, False), (324, False), (361, False), (400, False), (441, False), (484, False), (529, False), (576, False), (625, False), (676, False), (729, False), (784, False), (841, False), (907, True)]
    for n, exp in test_cases:
        assert_result("t1:\n" + str(n), exp, is_prime_standard(n))
        assert_result("t2:\n" + str(n), exp, is_prime(n))
