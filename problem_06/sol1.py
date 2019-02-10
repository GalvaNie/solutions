"""
Problem:

The sum of the squares of the first ten natural numbers is,
            1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
            (1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first N natural
numbers and the square of the sum.
"""


def solution(n):
    """Returns the difference between the sum of the squares of the first n
    natural numbers and the square of the sum.

    >>> solution(10)
    2640
    >>> solution(15)
    13160
    >>> solution(20)
    41230
    >>> solution(50)
    1582700
    """
    suma = 0
    sumb = 0
    for i in range(1, n + 1):
        suma += i ** 2
        sumb += i
    sum = sumb ** 2 - suma
    return sum


if __name__ == "__main__":
    print(solution(int(input().strip())))
