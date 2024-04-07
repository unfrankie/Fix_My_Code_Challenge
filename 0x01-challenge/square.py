#!/usr/bin/python3
""" Square Class"""


class square():
    """ Square Class"""    
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        """INIT"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def square_permiter(self):
        """Square permiter"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """STR"""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    """MAIN"""
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.square_permiter())
