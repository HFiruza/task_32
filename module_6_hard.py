import math

class Figure: # родительский
    sides_count = 0

    __sides = []# (список сторон (целые числа))
    __color = list() # (список цветов в формате RGB)
    filled = bool# (закрашенный, bool)

    def __init__(self, __color, __sides):
        self.__sides = []
        self.__color = list(__color)

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *new_sides):
        for self.__sides in new_sides:
            if not isinstance(new_sides, int) or side <= 0:
                return False
        return len(new_sides) == self.sides_count

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)
        else:
            return list(self.__sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, __sides):
        super().__init__(__color, __sides)
        self.__radius = self.sides_count / (2 * math.pi)

        # Вычисление длины окружности (это я для себя записала, на будущее)
        #self.sides_count = 2 * math.pi * self.__radius

        # Вычисление площади круга
        # A = math.pi * R ** 2

    def get_square(self):
        return math.pi * self.__radius ** 2 # вычисление площади круга

class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, __sides):
        super().__init__(__color, __sides)
        self.__sides = a, b, c

    def get_square(self): # по формуле Герона
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, edge):
        super().__init__(__color, edge)
        self.edge = edge
        self.set_sides(*[edge] * self.sides_count)

    def get_volume(self):
        return self.edge ** 3



# Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())



