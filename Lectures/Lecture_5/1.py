# Author: Anna Mikhailova
# Date: 09/22/21
# Purpose: Demo functions
# function name needs to start with a lowercase letter

# Purpose: To show the working fo parameters -- NEED TO HAVE THERE COMMENTS
# Parameter: A string parameter representing a course
def demo_func(course, term):  # Parameter has to be named, can't be a string etc.; these are positional parameters
    print("Welcome to", course, term)
    print("Are you having fun?")


# print("before the function call")
demo_func("CS1", "21F")
# demo_func("CS10")
# print("After the function call")

# def count_func():
#     n = 10
#     count = 0
#
#     while count < n:
#         print(count)
#         count += 1
#
# count_func()
# count_func()
# can call as many times as you want
