#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
from PIL import Image
import os


# ### Scenario B: Calculating Perimeters and Areas

# In[3]:


# Define the known regular polygons
regular_polygons = {
    3: "Triangle",
    4: "Square",
    5: "Pentagon",
    6: "Hexagon",
    7: "Heptagon"
}

# Constants for valid length range and child's hand size range
MIN_SIDE_LENGTH = 1
MAX_SIDE_LENGTH = 20
CHILD_HAND_SIZE_LOWER = 70.5
CHILD_HAND_SIZE_UPPER = 90.5

# Function to calculate the perimeter of a regular polygon
def calculate_perimeter(num_sides, side_length):
    if num_sides in regular_polygons:
        return num_sides * side_length
    else:
        return None

# Function to calculate the area of a regular polygon
def calculate_area(num_sides, side_length):
    if num_sides in regular_polygons:
        if num_sides == 3:  # Triangle
            # Implement the formula for the area of a triangle
            return (math.sqrt(3) / 4) * side_length ** 2
        elif num_sides == 4:  # Square
            # Implement the formula for the area of a square
            return side_length ** 2
        # Implement the area calculation for other polygons here
        else:
            apothem = side_length / (2 * math.tan(math.pi / num_sides))
            area = (num_sides * side_length * apothem) / 2
            return area
    else:
        return None

# Function to compare the calculated area with the given situations
def compare_area_with_situations(area):
    if area < CHILD_HAND_SIZE_LOWER:
        return "The shape size is smaller than a child's hand size."
    elif area > CHILD_HAND_SIZE_UPPER:
        return "The shape size is larger than a child's hand size."
    else:
        return "The shape size is close to a child's hand size."

# Main function for Scenario B
def main_scenario_b():
    side_length = float(input("Enter the length of a side (in centimeters): "))
    
    if side_length < MIN_SIDE_LENGTH or side_length > MAX_SIDE_LENGTH:
        print("Side length is outside the valid range.")
        return

    num_sides_or_shape = input("Enter the number of sides or polygon shape name: ")

    try:
        num_sides = int(num_sides_or_shape)
    except ValueError:
        num_sides = regular_polygons.get(num_sides_or_shape.title(), None)

    if num_sides is not None:
        perimeter = calculate_perimeter(num_sides, side_length)
        area = calculate_area(num_sides, side_length)

        if perimeter is not None and area is not None:
            print(f"Perimeter of the polygon: {perimeter} cm")
            print(f"Area of the polygon: {area} cm^2")

            area_message = compare_area_with_situations(area)
            print(area_message)
        else:
            print("Invalid number of sides or side length.")
    else:
        print("Invalid number of sides or unknown shape name.")

if __name__ == "__main__":
    main_scenario_b()

