def get_string_binary(n):
    """
    Function takes an input integer and converts it into a binary string
    :param n: Input integer
    :return: Binary string representation of input variable
    """
    string_value = bin(n)[2:]
    return string_value


def calculate(binary):
    """
    Calculates the number of binary gaps in a string which contains an integer in binary format
    :param binary: string input
    :return: number of binary gaps in string
    """
    index = -1
    max_diff = 0

    for i in range(len(binary)):
        if binary[i] == '1':
            if index > -1 and max_diff < i - index - 1:
                max_diff = i - index - 1
            index = i

    return max_diff


def solution(N):
    """
    The solution function of the lesson
    :param N: integer between 1 and (sg large)
    :return: number of binary gaps as according to lesson description
    """
    # Check if input is actually an integer
    if not isinstance(N, int):
        return -1

    # Check if integer is in range
    if N < 1:
        return 0

    # call the two functions which solve the problem
    string_form = get_string_binary(N)
    return calculate(string_form)

# For testing
# if __name__=="__main__":
#     input = 6020
#     # solution = Solution(input)
#     # print(solution.Calculate())
#     binary_format = get_string_binary(input)
#     print(binary_format)
#     print(calculate(binary_format))