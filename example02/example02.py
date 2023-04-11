class Point:
    def __init__(self, coordX, coordY):
        self.x_axis = x_axis
        self.y_axis = y_axis


class Rectangle:
    def __init__(self, origin, width, heigth):
        self.origin = origin
        self.width = width
        self.heigth = height

    def area(self):
        return self.width * self.height

    def print_coordinates(self):
        end_point_x_axis = self.origin.x_axis + self.width
        end_point_y_axis = self.origin.y_axis + self.height

        print('Starting Point X-Axis): ' + str(self.starting_point.coordX))
        print('Starting Point Y-Axis): ' + str(self.starting_point.coordY))
        print('End Point X-Axis: ' + str(end_point_x_axis))
        print('End Point Y-Axis: ' + str(end_point_y_axis))


def create_origin():
    origin = Point(50, 100)

def create_rectangle(main_point):
    rectangle = Rectangle(main_point, 90, 10)

    return rectangle

origin = create_origin()
rectangle = create_rectangle(origin)

print(rectangle.area())
rectangle.print_coordinates()