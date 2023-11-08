"""Method: Functions that operate on the attributes of a specific instance of a class"""
class Apple:
    def __init__(self,color,flavor):
        self.color = color
        self.flavor = flavor
Jonagold = Apple("Red","Sweet")
#
# print(Jonagold) Output will be: <__main__.Apple object at 0x0000021690D8B460>
# So, we need to add something

# -----------------------------------------------------------------------------------
class Apple:
    """This is docstring"""
    def __init__(self,color,flavor):
        """Define the color and flavor of the apple"""
        self.color = color
        self.flavor = flavor
    def __str__(self):
        """
        Return sentence if the class called without any attribute
        for example:
        Jonagold = Apple("Red","Sweet")
        print(Jonagold)
        """
        return (f"This apple is {self.color} and it's flavor is {self.flavor}")

Jonagold = Apple("Red","Sweet")
print(Jonagold)
help(Apple)