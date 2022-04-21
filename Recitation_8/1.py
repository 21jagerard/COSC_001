# Purpose: Define a function that takes a dictionary as a parameter. Inside the dictionary:
# keys: student net IDs (strings)
# values: student names (strings)
# return a new dictionary with names as keys and a positive integer as value giving the number of students with that
# name in original dictionary

net_id_dict = {"F00123": "Vasanta", "F00124": "Isaac", "F00125": "Kelly", "FOO126": "Vasanta", "F00127": "Isaac", "F00128": "Kelly"}

# Problem 1
def func1(dict):
    new_dict = {}
    count = 1
    for key in dict:
        if dict[key] in new_dict:
            new_dict[dict[key]] += 1
        else:
            new_dict[dict[key]] = count
    return new_dict

# print(func1(net_id_dict))

# Problem 2
def func2(glist):
    count = 1
    new_dict = {}
    for name in glist:
        if name in new_dict:
            new_dict[name] += 1
        else:
            new_dict[name] = count
    return new_dict

print(func2(["Apurva", "Isaac", "Kelly", "Vasanta", "Isaac", "Kelly"]))

# Problem 3
def func3(dict):
    for key in dict:
        print(dict[key])

# func3(net_id_dict)

