from util import assert_result


# remove_duplicates_simple :: Eq a => [a] -> [a]
# receives a list and returns another that is equal to the original, but without duplicate elements
# time complexity: XXXX     space complexity: YYYY
def remove_duplicates_simple(a_list):
    # raise NotImplemented
    length = len(a_list)
    i = 0
    while i < length:
        value = a_list[i]
        count = a_list.count(value)
        if count == 1:
            i += 1
        else:
            while count > 1:
                a_list.remove(value)
                count -= 1
                length -= 1
    return a_list


# remove_duplicates_improved :: Eq a => [a] -> [a]
# receives a list and changes it, removing duplicate elements
# time complexity: XXXX     space complexity: YYYY
def remove_duplicates_improved(a_list):
    a_list.sort()
    i = 1
    while i < len(a_list):
        if a_list[i - 1] == a_list[i]:
            a_list.remove(a_list[i-1])
        else:
            i += 1
    return a_list


# remove_duplicates :: Eq a => [a] -> [a]
# receives a list and changes it, removing duplicate elements
# time complexity: XXXX     space complexity: YYYY
def remove_duplicates(a_list):
    return list(set(a_list))


def test():
    l1 = [0, 47, 74, 38, 24, 64, 6, 85, 80, 20, 34, 75, 45, 13, 4, 87, 43, 29, 30, 27, 0, 25, 84, 77, 21, 38, 10, 59, 95, 18, 36, 86, 45, 65, 87, 49, 14, 47, 13, 63, 20, 50, 86, 23, 97, 34, 38, 95, 5, 26, 11, 91, 94, 63, 73, 21, 1, 88, 27, 36, 42, 76, 19, 43, 46, 35, 30, 62, 65, 5, 95, 73, 88, 87, 16, 6, 70, 60, 29, 63, 18, 63, 71, 12, 66, 43, 94, 61, 98, 47, 48, 42, 79, 22, 40, 57, 20, 9, 24, 34]
    l2 = [34, 99, 73, 84, 19, 81, 64, 91, 83, 10, 87, 9, 25, 27, 61, 76, 58, 47, 71, 14, 36, 89, 50, 49, 13, 6, 65, 30, 10, 64, 44, 41, 14, 66, 18, 94, 58, 61, 85, 68, 1, 62, 83, 80, 59, 44, 45, 21, 78, 2, 16, 14, 63, 76, 29, 46, 88, 7, 64, 72, 94, 45, 81, 96, 43, 9, 60, 61, 87, 71, 34, 23, 95, 46, 35, 98, 84, 17, 28, 68, 54, 36, 34, 44, 79, 92, 4, 90, 81, 27, 16, 70, 13, 62, 61, 87, 25, 51, 50, 47]

    test_cases = ([0, 47, 74, 38, 24, 64, 6, 85, 80, 20, 34, 75, 45, 0, 74, 47, 1, 1], l1, l2, [1, 2, 2, 2, 2, 2, 2, 2, 2],  [1, 5, 5, 5, 5, 5, 5],  [1, 2, 2, 2, 2, 2, 2, 2],  [1, 2, 2, 2, 2, 2, 2])
    no_error = True
    for l in test_cases:
        try:
            expected = set(l)
            out = set(remove_duplicates_simple(l.copy()))
            no_error = no_error or assert_result('t1:\n' + str(l), expected, out)
            out = set(remove_duplicates_improved(l.copy()))
            no_error = no_error or assert_result('t2:\n' + str(l), expected, out)
            out = set(remove_duplicates(l.copy()))
            no_error = no_error or assert_result('t3:\n' + str(l), expected, out)
        except NotImplementedError:
            pass

    if no_error:
        print("All test cases passed!")
