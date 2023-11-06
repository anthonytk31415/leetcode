# class inheritance

import math

class Quadrilateral:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width


class Square(Quadrilateral):
    def __init__(self, length, width) -> None:
        if length != width:
            raise Exception("length and width not equal")
        super().__init__(length, width)


class Triangle(Quadrilateral):
    def __init__(self, length, width) -> None:
        super().__init__(length, width)
        
    @property
    def perimeter(self):
        return 3*self.length

    @property
    def area(self):
        return math.sqrt(self.length*3/2 * (self.length*3/2 - self.length) ^ 3)




class Book:
    def __init__(self, title, author, year) -> None:
        self.title = title
        self.author = author
        self.year = year


    def description(self):
        return f"{self.title} is written by {self.author} and was published in {self.year}."
    
class NonfictionBook(Book):
    def __init__(self, title, author, year, subject) -> None:
        super().__init__(title, author, year)
        self.subject = subject

    def description(self):
        return f"{self.title} is written by {self.author} and was published in {self.year}. It is a nonfiction book about {self.subject}."


class StrNumeric:
    def __init__(self, value) -> None:
        if isinstance(value, str) and not (value.isnumeric()):
            raise Exception('it is a string but not a numerical string')
        self.val = value

    def __add__(self, thing_2):
        return int(self.val) + int(thing_2)