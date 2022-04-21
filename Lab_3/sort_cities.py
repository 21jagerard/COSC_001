# Author: Anna Mikhailova
# Date: 11/2/21
# Course: COSC_001
# Purpose: Lab 3; sorts cities alphabetically, by population, and by latitude

from Lab_3.quicksort import *
from city import City

# Purpose: compares the names of two cities
# Parameters: two strings, a and b
# Return: true if string a does not come after string b alphabetically
def compare_alpha(a, b):
    return a.name.lower() <= b.name.lower()

# Purpose: compares the populations of two cities
# Parameters: two integers, a and b
# Return: returns true if integer a is greater than or equal to integer b
def compare_pop(a, b):
    return a.population >= b.population

# Purpose: compares the latitudes of two cities
# Parameters: two floats, a and b
# Return: returns true if float a is less than or equal to integer b
def compare_lat(a, b):
    return a.latitude <= b.latitude

world_cities_fp = open("world_cities.txt", "r")

world_cities_list = []

# creates a City object for each line of the world_cities.txt file and appends it to the world_cities_list
for line in world_cities_fp:
    city_info = line.strip("\n")
    clist = city_info.split(",")
    name = City(clist[0], clist[1], clist[2], clist[3], clist[4], clist[5])
    world_cities_list.append(name)

cities_alpha_w = open("cities_alpha.txt", "w")
sort(world_cities_list, compare_alpha)  # sorts world_cities_list alphabetically, from A-Z

# calls the __str__ method of each City object in the sorted world_cities_list
# to write the city's info into cities_alpha.txt
for city in world_cities_list:
    cities_alpha_w.write(str(city) + "\n")

cities_alpha_w.close()

cities_population_w = open("cities_population.txt", "w")
sort(world_cities_list, compare_pop)  # sorts the world_cities_list by population, from greatest to least

# calls the __str__ method of each City object in the sorted world_cities_list
# to write the city's info into cities_population.txt
for city in world_cities_list:
    cities_population_w.write(str(city) + "\n")

cities_population_w.close()

cities_latitude_w = open("cities_latitude.txt", "w")
sort(world_cities_list, compare_lat)  # sorts the world_cities_list by latitude from south to north

# calls the __str__ method of each City object in the sorted world_cities_list
# to write the city's info into cities_latitude.txt

for city in world_cities_list:
    cities_latitude_w.write(str(city) + "\n")

cities_latitude_w.close()

world_cities_fp.close()