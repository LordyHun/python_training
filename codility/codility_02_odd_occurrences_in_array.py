def array_to_dict(n):
    """
    Converts a list to a dict where keys are the values of elements and the values are the number of occurrences of each value
    :param n: input list
    :return: dict of occurrences
    """
    transformed = dict()
    for element in n:
        if element not in transformed:
            transformed[element] = 1
        else:
            transformed[element] += 1

    return transformed


def get_odd_from_dict(n):
    """
    Returns with the first (according to spec, only) value from the dict where the number of occurrences is an odd number
    :param n:
    :return:
    """
    for key in n:
        if n[key] % 2 != 0:
            return int(key)


def solution(A):
    # write your code in Python 3.6
    mydiict = array_to_dict(A)
    sol = get_odd_from_dict(mydiict)
    return sol


# For testing
# if __name__=="__main__":
#     input = [1, 2, 2, 1, 3, 4, 5, 4, 3]
#     # solution = Solution(input)
#     # print(solution.Calculate())
#     mydiict = array_to_dict(input)
#     print(mydiict)
