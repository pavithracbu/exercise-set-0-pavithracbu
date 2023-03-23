"""
ex_0_5.py

Write a Python module named ex_0_5.py that solves the following problem. 
The Global Historical Climatology Network uses a fixed length file format. 
NOAA uses this format for reporting daily ground station data. 
The format specification can be found here. For this exercise, we are only interested in one element, Minimum soil temperature.
Minimum soil temperature (and maximum soil temperature) elements are fixed length fields which begin with 
SN and end with a two character code representing ground cover and depth code. 
In this exercise, you will extract these codes from the text element and return them as integers.

1. Function ground_cover takes one positional string argument and returns the ground cover code as an integer.
2. Function depth takes one positional string argument and returns the depth code as an integer.

"""



#Function ground_cover takes one positional string argument and returns the ground cover code as an integer.

def ground_cover(minimum_soil_temperature):
    return(int(minimum_soil_temperature[2]))

#Function depth takes one positional string argument and returns the depth code as an integer.

def depth(minimum_soil_temperature):
    return (int(minimum_soil_temperature[3]))

minimum_soil_temperature = 'SN07'


ground_cover(minimum_soil_temperature)
depth(minimum_soil_temperature)