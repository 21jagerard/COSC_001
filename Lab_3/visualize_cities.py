# Author: Anna Mikhailova
# Date: 11/2/21
# Course: COSC_001
# Purpose: Lab 3; draws top 50 most populous cities on a world map

from cs1lib import *
from Lab_3.city import City

WIDTH = 720
HEIGHT = 360
i = 0
first_clear = True

cities_population_fp = open("cities_population.txt", "r")
img = load_image("world.png")

world_cities_list = []

# Purpose: draws a red circle centered at the latitude and longitude coordinates of the city
# Parameters: x and y coordinates of the center of the circle
def draw_city_marker(lat, long):
    set_fill_color(1, 0, 0)
    draw_circle(long, lat, 3)

# creates a latitude, longitude list for each line of the world_cities.txt file and appends it to the world_cities_list
for line in cities_population_fp:
    city_info = line.strip("\n")
    clist = city_info.split(",")
    long = HEIGHT // 2 - (HEIGHT * float(clist[2]) / 90) // 2
    lat = WIDTH // 2 + (WIDTH * float(clist[3]) / 180) // 2
    world_cities_list.append([long, lat])

# Purpose: main draw function; draws the 50 most populous cities one by one
# Parameters: none
def main():
    global i, first_clear
    if first_clear:  # only draws the map once, so that the city markers are not erased after the first 50 cities
        draw_image(img, 0, 0)
        first_clear = not first_clear
    if i <= 50:
        for city in range(0, i):
            y = float(world_cities_list[city][0])
            x = float(world_cities_list[city][1])
            draw_city_marker(y, x)
        i += 1

start_graphics(main, width=WIDTH, height=HEIGHT, framerate=10)

cities_population_fp.close()