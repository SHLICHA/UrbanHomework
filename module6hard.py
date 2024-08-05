from math import pi, sqrt

class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled = True):
        self.__color: list = list(color)
        if len(sides) != self.sides_count:
            sides = [1 for i in range(self.sides_count)]
        self.__sides = [side for side in sides]
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if (0 <= r <= 255) and (0 <= g <= 255) and (0 <= b <= 255):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        if len(args) == self.sides_count:
            for i in args:
                if i <= 0:
                    return False
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        perimeter = 0
        for x in self.__sides:
            perimeter += x
        return perimeter


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *args, filled = True):
        super().__init__(color, args, filled)
        self.__radius: float = args[0] / (2 * pi)

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *args, filled = True):
        super().__init__(color, args, filled)
        p = sum(self.get_sides()) / 2
        self.__height = 2 * sqrt(p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2])) / args[0]

    def get_square(self):
        return 0.5 * self.get_sides()[0] * self.__height


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *args, filled = True):
        if len(args) > 1:
            sides = [1 for i in range(12)]
        else:
            sides = [args[0] for i in range(12)]
        super().__init__(color, sides, filled)

    def get_volume(self):
        return 6 * self.get_sides()[0] ** 2


circle1 = Circle((200, 200, 100), 10)
print(f"Стороны круга: {circle1.get_sides()}")
cube1 = Cube((222, 35, 130), 6)
print(f"Стороны куба: {cube1.get_sides()}")
tr1 = Triangle((22, 200, 100), 2, 2)
print(f"Стороны треугольника (задано неверное количество сторон): {tr1.get_sides()}")
circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())
