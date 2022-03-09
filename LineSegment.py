#Name: Lilliana Parra
#Date: 3/8/2022
#Github user: ParraL1
#Description: takes two points and finds the distance between them


# defining class Point
import math


class Point:
    # constructor
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord

    # get x_coordinate
    def get_x_coord(self):
        return self.x_coord

    # get y coordinate
    def get_y_coord(self):
        return self.y_coord

    # get distance between two points
    def distance_to(self, point_2):
        return math.sqrt(abs((point_2.x_coord - self.x_coord) ** 2 + (point_2.y_coord - self.y_coord) ** 2))

#class Line
class LineSegment:
    # constructor
    def __init__(self, point_1, point_2):
        self.endpoint_1 = point_1
        self.endpoint_2 = point_2

    # get first endpoint
    def get_endpoint_1(self):
        return self.endpoint_1

    # get second endpoint
    def get_endpoint_2(self):
        return self.endpoint_2

    # return the length of line segment
    def length(self):
        return self.endpoint_1.distance_to(self.endpoint_2)

    # check if two lines are parallel
    def is_parallel_to(self, line_segment):
        if self.slope() == line_segment.slope():
            return True
        else:
            return False

    # calculate slope of line
    def slope(self):
        return (self.endpoint_2.get_y_coord() - self.endpoint_1.get_y_coord()) / (
                self.endpoint_2.get_x_coord() - self.endpoint_1.get_x_coord())
