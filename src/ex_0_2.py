"""
ex_0_2.py

Write a Python script named ex_0_2.py that implements the following:

Assign the text addison to a variable named 'first_name'
Assign the text bellamy to a variable named 'last_name'
Concatenate first_name, followed by a space, followed by last_name and assign the result to the variable full_name.
Use the appropriate string method on full_name so that the first letter of each name is capitalized. Assign this value to a variable name full_name_title.
Print the contents of the full_name_title variable.

"""
first_name = 'addison'
last_name = 'bellamy'

full_name = first_name + ' ' + last_name

full_name_title = full_name.title()

print(full_name_title)
