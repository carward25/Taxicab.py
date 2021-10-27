#name: Cassidy Ward
#date: 10/26/2021
#description: program that holds three private data members for x, y coordinates and current odometer reading

class Taxicab:
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y
        self.odometer = 0

    def move_x(self, value):
        self.x_coord += value
        self.odometer += abs(value)

    def move_y(self, value):
        self.y_coord += value
        self.odometer += abs(value)

    def get_x_coord(self):
        return self.x_coord

    def get_y_coord(self):
        return self.y_coord

    def get_odometer(self):
        return self.odometer
