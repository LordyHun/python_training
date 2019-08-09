# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    total = sum(A)
    minimum = float('inf')
    left_sum = 0
    for i in A[:-1]:
        left_sum += i
        minimum = min(abs(total - 2*left_sum), minimum)
    return minimum