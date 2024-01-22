
from coordinates import Point, Rectangle

MAX_COORDINATES = 100;

bottom_left_point = Point.get_random_point(0, MAX_COORDINATES, 0, MAX_COORDINATES)
upper_right_point = Point.get_random_point(
    bottom_left_point.x + 1,
    bottom_left_point.x + MAX_COORDINATES, 
    bottom_left_point.y + 1,
    bottom_left_point.y + MAX_COORDINATES)

rect = Rectangle(bottom_left_point, upper_right_point)

print(f"Rectangle coordinates are: {rect.bottom_left} for bottom left and and {rect.upper_right} for upper right")

user_point = Point(int(input("Guess X: ")), int(input("Guess Y: ")))

print(f"Your point is inside the rectangle: {rect.is_point_in_rectangle(user_point)}")