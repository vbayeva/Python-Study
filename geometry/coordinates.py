from random import randint

class Point():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y
    
    def __lt__(self, other):
        return self.x < other.x and self.y < other.y
    
    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y
    
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
    
    def __repr__(self) -> str:
        return f"{self.x} and {self.y}"
    
    def get_random_point(
            min_coordinates_x: int, 
            max_coordinates_x: int,
            min_coordinates_y: int,
            max_coordinates_y: int):
        return Point(randint(min_coordinates_x, max_coordinates_x), 
                     randint(min_coordinates_y, max_coordinates_y))
    

class Rectangle():
    def __init__(self, bottom_left: Point, upper_right: Point):
        self.upper_right = upper_right
        self.bottom_left = bottom_left

    def is_point_in_rectangle(self, point: Point) -> bool:
        if self.bottom_left <= point and self.upper_right >= point:
            return True
        return False
