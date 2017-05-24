"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

while True:
    ops_and_nums = raw_input("> ")
    ops_and_nums = ops_and_nums.split(" ")
    first_num = int(ops_and_nums[1])
    second_num = int(ops_and_nums[2])
    if ops_and_nums[0] == "q":
        break
    elif ops_and_nums[0] == "+":
        # first_num = int(ops_and_nums[1])
        # second_num = int(ops_and_nums[2])
        print add(first_num, second_num)
    elif ops_and_nums[0] == "-":
        print subtract(first_num, second_num)
    elif ops_and_nums[0] == "*":
       print multiply(first_num, second_num)