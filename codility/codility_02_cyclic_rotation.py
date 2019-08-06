from collections import deque

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A, K):
    """
    Solves the lesson by using Python's deque class which has an interface for rotation
    :param A: input list
    :param K: number of rotations
    :return:
    """
    # write your code in Python 3.6
    items = deque(A)
    items.rotate(K)

    return list(items)

