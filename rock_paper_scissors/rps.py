#!/usr/bin/python

import sys
import math


def rock_paper_scissors(n):
    outer_list = []
    inner_list = []

    def helper(rounds_left, list):
        print("N:", rounds_left)
        if rounds_left < 1:
            outer_list.append(list)
            # print("We're in..", outer_list)
            list = []
            return outer_list

        else:
            options = ['rock', 'paper', 'scissors']
            for option in range(len(options)):
                # print("Option:", option)
                # print("options[option]:", options[option])
                # print("Inner list =>", inner_list)
                # inner_list.append(options[option])
                helper(rounds_left - 1, list + [options[option]])

    helper(n, inner_list)
    return outer_list


# print(rock_paper_scissors(0))
# print(rock_paper_scissors(2))
# print(rock_paper_scissors(2))
print(rock_paper_scissors(3))


# factorial_memo = {}

# def factorial(k):
#     if k < 2:
#         return 1
#     if k not in factorial_memo:
#         print(factorial_memo)
#         factorial_memo[k] = k * factorial(k-1)
#     return factorial_memo[k]


# def rock_paper_scissors(n):
#     my_list = []

#     def helper(helper_input):
#         if helper_input == 0:
#             my_list.append([])
#             return my_list

#         # make length of my_list correct - should be 3x the previous
#         # array
#         else:
#             # print("My list ==>", my_list)
#             # for item in range(3 ** count - 1):
#             # length = len(my_list)
#             # for item in range(length):
#             options = ['rock', 'paper', 'scissors']
#             for option in options:
#                 my_list + [option]
#                 print("my_list =>", my_list)
#                 # my_list.append(my_list[item])
#                 # my_list.insert(item, my_list[item])
#                 # my_list.insert(0, item)
#             # mid = math.ceil(len(my_list) / 2)
#             # for item in range(3 ** count - 1):
#             #     print("Item paper=>", item, my_list[item])
#             #     my_list.insert(mid, ['paper'])
#             # for item in range(3 ** count - 1):
#             #     print("Item scissors=>", item, my_list[item])
#             #     my_list.insert(-1, ['scissors'])

#         # Add rock paper scissors to my_list with the correct
#         # length of overall list, but incorrect length of
#         # individual lists

#         # options = ['rock', 'paper', 'scissors']
#         # options_count = 0
#         # for item in range(len(my_list)):
#         #     # print("Item --", my_list[item])
#         #     my_list[item].append(options[options_count])
#         #     if options_count == 2:
#         #         options_count = 0
#         #     else:
#         #         options_count += 1
#         print("helper_input", helper_input)
#         helper(helper_input - 1)
#     helper(n, inner_list)
#     return my_list


# print(rock_paper_scissors(0))
print(rock_paper_scissors(1))
# print(rock_paper_scissors(2))
# print(rock_paper_scissors(3))
# print(rock_paper_scissors(4))

# if n == 0:
#     return my_list
# else:
#       # if len(my_list[0]) != n:
#     # for i in range(3**(n-1)):
#     #     my_list.append(['rock'])
#     # for i in range(3**(n-1)):
#     #     my_list.append(['paper'])
#     # for i in range(3**(n-1)):
#     #     my_list.append(['scissors'])
#     rock_index = my_list.index(['rock'])
#     paper_index = my_list.index(['paper'])
#     scissors_index = my_list.index(['scissors'])
#     for item in range(len(my_list) - 1):
#         # print("Item:", item)
#         my_list.insert(rock_index, ['rock'])
#         my_list.insert(paper_index, ['paper'])
#         my_list.insert(scissors_index, ['scissors'])
#         print("MY list", my_list)
#     if len(my_list[0]) == n:
#         return my_list
# return my_list


# print(factorial(3))
# print(factorial(4))
# print(factorial(10))


# , [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], [
#  'paper', 'paper'], ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
