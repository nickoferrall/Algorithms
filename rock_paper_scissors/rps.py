#!/usr/bin/python

import sys
import math


def rock_paper_scissors(n):
    outer_list = []
    inner_list = []

    def helper(rounds_left, list):
        if rounds_left < 1:
            outer_list.append(list)
            list = []
            return outer_list

        else:
            options = ['rock', 'paper', 'scissors']
            for option in range(len(options)):
                helper(rounds_left - 1, list + [options[option]])

    helper(n, inner_list)
    return outer_list


# print(rock_paper_scissors(0))
print(rock_paper_scissors(2))
# print(rock_paper_scissors(2))
# print(rock_paper_scissors(3))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
