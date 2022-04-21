# Author: Anna Mikhailova
# Date: 10/31/21
# Course: COSC_001
# Purpose: Lab 3; class file for City class;

class City:
    def __init__(self, gcode, gname, greg, gpop, glat, glon):
        self.code = gcode
        self.name = str(gname)
        self.region = greg
        self.population = int(gpop)
        self.latitude = float(glat)
        self.longitude = float(glon)

    # The __str__ method returns a string consisting of the city's name, population, latitude, and longitude,
    # separated by commas and with no spaces around the commas.
    def __str__(self):
        return self.name + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longitude)
