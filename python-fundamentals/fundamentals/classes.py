# classes

class AngryBird:
    __slots__ = ['_x', '_y', '_z']

    def __init__(self, x=0, y=0, z=0):
        """
        Construct a new AngryBird by setting its position to (0, 0).
        """
        self._x = x
        self._y = y
        self._z = z

    def move_up_by(self, delta):
        self._y += delta

    @property
    def x(self):
        return self._x
    
    @x.setter
    def set_x(self, value):
        if value < 0:
            value = 0
        self._x = value
    
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if value < 0:
            value = 0
        self._y = value

    def z(self):
        return self._z

    


bird = AngryBird()

print(f'x: {bird.x}, y: {bird.y}')
print(f'z: {bird.z()}')

bird.set_x = 12
bird.y = -99
print(f'x: {bird.x}, y: {bird.y}')

# getters and setters properties: 
# normally you have to do do (bird.x(), bird.y()) with the '()' on methods to call the method, but with 
# properties (getters, setters), you won't have to:

# '_' denotes variables that are properties and are important; you put them in __slot__ to access them faster




#### practice 
class RegularPolygon:
    def __init__(self, num_sides, length):
        if num_sides < 3:
            raise Exception("A polygon must have at least 3 sides.")

        self.num_sides = num_sides
        self.length = length
        self.type = 'Polygon'

    def identify_polygon(self):
        type_dict = {
            3: "Triangle",
            4: "Quadrilateral",
            5: "Pentagon",
            6: "Hexagon",
            7: "Heptagon",
            8: "Octagon",
            9: "Nonagon",
            10: "Decagon",
        }
        try:
            self.type = type_dict[self.num_sides]
        except KeyError:
            self.type = f'Polygon with {self.num_sides} sides'

    @classmethod
    def polygon_factor(cls, list_of_tuples):
        return [cls(x,y) for x,y in list_of_tuples]

    
    @staticmethod
    def get_perimeter(self):
        return self.num_sides * self.length