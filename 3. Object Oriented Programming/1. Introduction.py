"""
Attribute: Characteristics associate with a type
Method: Functions that operate on the attributes of a specific instance of a class

python have default classes such as int, float, char, str
to find all of attribute that class have, just type help(...), ex: help(""),help(int)
"""


# Define Class
class Apple:
    color = ""  # A string
    flavor = " "  # also a string


Jonagold = Apple()
Jonagold.color = "red"
Jonagold.flavor = "sweet"
print(Jonagold.color, Jonagold.flavor.upper())
