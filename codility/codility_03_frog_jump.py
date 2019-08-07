# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    """
    Solves the lesson.
    :param X: starting position
    :param Y: desired position
    :param D: jump distance
    :return:
    """
    distance_min = Y - X
    number_of_jumps = int(distance_min / D)
    # handle fractions
    if (X + number_of_jumps * D) < Y:
        number_of_jumps += 1

    return number_of_jumps
