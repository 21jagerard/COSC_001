# Define a function that takes a string str as a parameter and returns a string that is the reverse of the given string.

def func(str):
    new_str = ""
    for i in str:
        new_str = i + new_str
    print(new_str)

func("dartmouth")
