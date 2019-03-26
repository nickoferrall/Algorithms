#!/usr/bin/python

import sys

# my_list = [['rock'], ['paper'], ['scissors']]

# my_list = []


def rock_paper_scissors(n):
    my_list = [['rock'], ['paper'], ['scissors']]
    count = 1

    def helper(helper_input, my_list, count):
        print("Input:", helper_input)
        # count = 0
        print("count:", count)
        if count == helper_input:
            print("In base case")
            return my_list
        else:
            print("helper_input 1st:", helper_input)
            print("count 2nd:", count)
            # helper_input -= 1

            print("count 3rd:", count)
            print("helper_input 2nd", helper_input)
            print("List 1st:", my_list)
            rock_index = my_list.index(['rock'])
        for item in range(3 ** count - 1):
            print("Item", item)
            my_list.insert(rock_index, ['rock'])
        paper_index = my_list.index(['paper'])
        for item in range(3 ** count - 1):
            my_list.insert(paper_index, ['paper'])
        scissors_index = my_list.index(['scissors'])
        for item in range(3 ** count - 1):
            my_list.insert(scissors_index, ['scissors'])
        print("My list:", my_list)
        options = ['rock', 'paper', 'scissors']
        options_count = 0
        for item in range(len(my_list)):
            print("Item --", my_list[item])
            my_list[item].append(options[options_count])
            if options_count == 2:
                options_count = 0
            else:
                options_count += 1
        count += 1
        helper(helper_input, my_list, count)
    helper(n, my_list, count)
    return my_list


# print(rock_paper_scissors(1))
print(rock_paper_scissors(2))
# print(rock_paper_scissors(3))

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


# factorial_memo = {}

# def factorial(k):
#     if k < 2:
#         return 1
#     if k not in factorial_memo:
#         print(factorial_memo)
#         factorial_memo[k] = k * factorial(k-1)
#     return factorial_memo[k]


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
