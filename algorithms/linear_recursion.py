from util import assert_result


# find_greatest :: Ord a => [a] -> a
# given a list of an orderable type, return the greatest element of the list
# without for loop!
# time complexity: O(n)  space complexity: O(n) (recursion stack)
def find_greatest(a_list):
    if len(a_list) == 0:
        return None
    if len(a_list) == 1:
        return a_list[0]
    else:
        return max(a_list[0], find_greatest(a_list[1:]))


# time complexity: O(n)  space complexity: O(logn) (recursion stack)
def find_greatest2(a_list):
    if len(a_list) == 0:
        return None
    if len(a_list) == 1:
        return a_list[0]
    else:
        mid = len(a_list)//2
        return max(find_greatest(a_list[:mid]), find_greatest(a_list[mid:]))


def test():
    test_cases = (list(range(9000)), [2, 5, 502, 5056, 204, 4021, 4054, 650, 406, 201931, 305, 602, 3])
    for test_case in test_cases:
        if not assert_result(test_case, find_greatest2(test_case), max(test_case)):
            break  # stop testing

