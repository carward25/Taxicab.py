#name: Cassidy Ward
#date: 10/26/2021
#description: program that holds three private data members for x, y coordinates and current odometer reading



class Taxicab:


def __init__(self, x, y):
    self.__x = x


self.__y = y
self.__odometer = 0


def get_x(self):
    return self.__x


def get_y(self):
    return self.__y


def get_odometer(self):
    return self.__odometer


def move_x(self, x):
    self.__x = self.__x + x


self.__odometer = self.__odometer + abs(x)


def move_y(self, y):
    self.__y = self.__y + y


self.__odometer = self.__odometer + abs(y)

cab = Taxicab(5, -8)
cab.move_x(3)
cab.move_y(-4)
cab.move_x(-1)
print(cab.get_odometer())