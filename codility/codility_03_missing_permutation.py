# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if not A:
        return 1

    N = len(A)
    # calculate the sum of permutation
    sum = int(((N + 1) * (N + 2)) / 2)

    for i in range(N):
        # iterate through the list, subtract the value of each element
        sum -= A[i]

    # the remaining sum will be the missing element
    return sum