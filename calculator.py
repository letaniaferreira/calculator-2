"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

while True:
    ops_and_nums = raw_input("> ")
    ops_and_nums = ops_and_nums.split(" ")
    operator = ops_and_nums[0]
    first_num = int(ops_and_nums[1])
    if len(ops_and_nums) == 3:
        second_num = int(ops_and_nums[2])
    if operator == "q":
        break
    elif operator == "+":
        print add(first_num, second_num)
    elif operator == "-":
        print subtract(first_num, second_num)
    elif operator == "*":
        print multiply(first_num, second_num)
    elif operator == "/":
        print divide(first_num, second_num)
    elif operator == "square":
        print square(first_num)
    elif operator == "cube":
        print cube(first_num)
