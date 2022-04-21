# Author: Anna Mikhailova
# Date: 10/31/21
# Course: COSC_001
# Purpose: Lab 3; driver file for City class;

from Lab_3.city import City

world_cities_fp = open("world_cities.txt", "r")
world_cities_list = []

# creates a City object for each line of the world_cities.txt file and appends it to the world_cities_list
for line in world_cities_fp:
    city_info = line.strip("\n")
    clist = city_info.split(",")
    name = City(clist[0], clist[1], clist[2], clist[3], clist[4], clist[5])
    world_cities_list.append(name)

cities_output_w = open("cities_out.txt", "w")

# calls the __str__ method of each City object in world_cities_list to write the city's info into cities_out.txt
for city in world_cities_list:
    cities_output_w.write(str(city) + "\n")

cities_output_w.close()

world_cities_fp.close()
