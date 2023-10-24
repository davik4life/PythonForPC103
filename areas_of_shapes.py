import math
ask_user = True

# Computes the area of a square


def compute_area_square(area):
    # area_calc = float(area) * float(area)
    area_calc = compute_area_rectangle(area, area)
    return area_calc

# Computes the area of a rectangle


def compute_area_rectangle(rect_width, rect_length):
    rect_calc = float(rect_width) * float(rect_length)
    return rect_calc

# Computes the area of a circle


def compute_area_circle(rad_squared):
    circ_calc = math.pi * float(rad_squared)
    return circ_calc


while ask_user:
    what_shape = input("What kind of shape do you have? ")
    if what_shape.lower() == "square":
        # prompt the user for the side of a square and save it into a variable
        ask_area = float(input("Enter the side of a square: "))
        # Pass the above variable to the above function to be able to calculate the area
        area_result = compute_area_square(ask_area)
        print(area_result)
        print()
    elif what_shape.lower() == "rectangle":
        ask_rect_width = float(input("What is the Width of the Rectangle: "))
        ask_rect_length = float(input("What is the Length of the Rectangle: "))
        rect_result = compute_area_rectangle(ask_rect_width, ask_rect_length)
        print(rect_result)
        print()
    elif what_shape.lower() == "circle":
        ask_circ = float(input("What is the Radius of the Circle: "))
        circ_result = compute_area_circle(ask_circ)
        print(circ_result)
        print()
    elif what_shape.lower() == "quit":
        ask_user = False
