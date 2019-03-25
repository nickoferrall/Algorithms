#!/usr/bin/python

import sys


def climbing_stairs(n, cache=None):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        # print("climbing_stairs n-1", climbing_stairs(n-1))
        # print("climbing_stairs n-2", climbing_stairs(n-2))
        # print("climbing_stairs n-3", climbing_stairs(n-3))
        return climbing_stairs(n - 1) + climbing_stairs(n - 2) + climbing_stairs(n - 3)


# print(climbing_stairs(3))  # 4
print(climbing_stairs(5))  # 13
print(climbing_stairs(6))  # 24
# print(climbing_stairs(10))  # 274

factorial_memo = {}


def factorial(k):
    if k < 2:
        return 1
    if k not in factorial_memo:
        print(factorial_memo)
        factorial_memo[k] = k * factorial(k-1)
    return factorial_memo[k]


# print(factorial(5))
# print(factorial(6))
# print(factorial(100))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_stairs = int(sys.argv[1])
        print("There are {ways} ways for a child to jump {n} stairs.".format(
            ways=climbing_stairs(num_stairs), n=num_stairs))
    else:
        print('Usage: climbing_stairs.py [num_stairs]')
