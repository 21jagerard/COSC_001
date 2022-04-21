def is_suffix(str1, str2, i=0):
    # base case
    if len(str1) > len(str2):
        return False
    if i == len(str1):  # checks if the amount of correct letters match
        return True
    # recursive case
    if str1[i] == str2[(len(str2)-len(str1)) + i]:  # check the correct letters in the word
        return is_suffix(str1, str2, i + 1)
    else:
        return False

print(is_suffix("washer", "dishwasher"))
print(is_suffix("wash", "dishwasher"))
print(is_suffix("", "test"))
print(is_suffix("test", ""))
print(is_suffix("", ""))
print(is_suffix("test", "test"))