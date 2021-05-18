#!/usr/bin/python3
"""Description"""


class Square():
    """Description"""

    def __init__(self, *args, **kwargs):
        """Description"""
        self.width = 0
        self.height = 0
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiterOfMySquare(self):
        """Description"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Description"""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiterOfMySquare())
