from util import assert_result


# get_common_elements_simple :: Eq a => [a], [a] -> [a]
# given two lists of a type we can check for equality, returns a list with only elements present in both
# time complexity: XXXX     space complexity: YYYY
def get_common_elements_simple(list1, list2):
    raise NotImplementedError


# get_common_elements_simple :: Eq a => [a], [a] -> [a]
# given two lists of a type we can check for equality, returns a list with only elements present in both
# time complexity: XXXX     space complexity: YYYY
def get_common_elements_improved(list1, list2):
    raise NotImplementedError

# get_common_elements_simple :: Eq a => [a], [a] -> [a]
# given two lists of a type we can check for equality, returns a list with only elements present in both
# time complexity: XXXX     space complexity: YYYY
def get_common_elements(list1, list2):
    raise NotImplementedError


def test():
    l1 = [0, 47, 74, 38, 24, 64, 6, 85, 80, 20, 34, 75, 45, 13, 4, 87, 43, 29, 30, 27, 0, 25, 84, 77, 21, 38, 10, 59, 95, 18, 36, 86, 45, 65, 87, 49, 14, 47, 13, 63, 20, 50, 86, 23, 97, 34, 38, 95, 5, 26, 11, 91, 94, 63, 73, 21, 1, 88, 27, 36, 42, 76, 19, 43, 46, 35, 30, 62, 65, 5, 95, 73, 88, 87, 16, 6, 70, 60, 29, 63, 18, 63, 71, 12, 66, 43, 94, 61, 98, 47, 48, 42, 79, 22, 40, 57, 20, 9, 24, 34]
    l2 = [34, 99, 73, 84, 19, 81, 64, 91, 83, 10, 87, 9, 25, 27, 61, 76, 58, 47, 71, 14, 36, 89, 50, 49, 13, 6, 65, 30, 10, 64, 44, 41, 14, 66, 18, 94, 58, 61, 85, 68, 1, 62, 83, 80, 59, 44, 45, 21, 78, 2, 16, 14, 63, 76, 29, 46, 88, 7, 64, 72, 94, 45, 81, 96, 43, 9, 60, 61, 87, 71, 34, 23, 95, 46, 35, 98, 84, 17, 28, 68, 54, 36, 34, 44, 79, 92, 4, 90, 81, 27, 16, 70, 13, 62, 61, 87, 25, 51, 50, 47]

    test_cases = ((l1, l2), ([1, 2, 2, 2, 2, 2, 2, 2, 2],  [1, 5, 5, 5, 5, 5, 5]),  ([1, 2, 2, 2, 2, 2, 2, 2],  [1, 2, 2, 2, 2, 2, 2]))
    for l1, l2 in test_cases:
        try:
            intersection = set(l1).intersection(l2)
            assert_result(str(l1) + '\n' + str(l2), intersection, set(get_common_elements_simple(l1, l2)))
            assert_result(str(l1) + '\n' + str(l2), intersection, set(get_common_elements_improved(l1, l2)))
            assert_result(str(l1) + '\n' + str(l2), intersection, set(get_common_elements(l1, l2)))
        except NotImplemented:
            pass