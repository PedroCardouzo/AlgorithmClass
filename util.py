def assert_result(test_case, expected, actual, log=False):
    if log:
        print(actual)
    if expected != actual:
        print("test case " + str(test_case) + "\nfailed:\nexpected = " + str(expected) + "\nactual   = " + str(actual), end='\n*******************************\n')
        return False
    return True


def timeit(f):
    import time
    start = time.time()
    out = f()
    end = time.time()
    elapsed = (end-start)
    print('elapsed time = ' + str(elapsed))
    return out, elapsed