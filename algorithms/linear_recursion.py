from util import assert_result


# find_greatest :: Ord a => [a] -> a
# given a list of an orderable type, return the greatest element of the list
# without for loop!
def find_greatest(a_list):
    raise NotImplementedError


def test():
    test_cases = (list(range(9000)), [2, 5, 502, 5056, 204, 4021, 4054, 650, 406, 201931, 305, 602, 3])
    try:
        for test_case in test_cases:
            if not assert_result(test_case, find_greatest(test_case), max(test_case)):
                break  # stop testing
    except NotImplementedError:
        pass
