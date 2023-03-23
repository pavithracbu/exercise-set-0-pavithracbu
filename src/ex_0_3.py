"""
ex_0_3.py

Write a Python script that contains a function format_name that takes two positional arguments first and last. 
The function should return the full name in appropriate name casing (as in ex_0_2.py).

Note: your script should not print anything

"""

first = 'addison'
last = 'bellamy'

def format_name(first, last):
    full_name = first + ' ' + last
    return full_name.title()
