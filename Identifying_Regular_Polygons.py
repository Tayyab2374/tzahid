#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
from PIL import Image
import os


# ### Scenario A: Identifying Regular Polygons

# In[2]:


# Define the known regular polygons
regular_polygons = {
    3: "Triangle",
    4: "Square",
    5: "Pentagon",
    6: "Hexagon",
    7: "Heptagon"
}

# Path to the "ISEimages" folder (change this to your actual path)
image_folder = "C:/Users/Teacher/Downloads/Assignment1/ISEimages"

# Scenario A: Finding the shape of a regular polygon
def find_polygon_shape(sides):
    if sides > 7:
        return "Number is too big"
    elif sides == 0 or sides == 1 or sides == 2:
        return "Number is too small"
    elif sides < 0:
        return "Negative number of sides is not valid"
    elif sides in regular_polygons:
        return regular_polygons[sides]
    else:
        return "Unknown"

# Display an image of a regular polygon from the "ISEimages" folder
def display_polygon_image(polygon_name):
    if polygon_name == "Number is too big" or polygon_name == "Number is too small" or polygon_name == "Negative number of sides is not valid":
        print(polygon_name)
    else:
        try:
            image_path = f"{image_folder}/{polygon_name}.png"
            img = Image.open(image_path)
            img.show()
        except FileNotFoundError:
            print(f"Image for {polygon_name} not found.")

# Main function
def main():
    # Input: Number of sides (change this to your desired input method)
    num_sides = int(input("Enter the number of sides: "))

    # Scenario A: Finding the shape of a regular polygon
    polygon_name = find_polygon_shape(num_sides)
    if polygon_name != "Unknown":
        print(f"The shape of a {num_sides}-sided polygon is: {polygon_name}")
        display_image = input("Do you want to display an image? (yes/no): ")
        if display_image.lower() == "yes":
            display_polygon_image(polygon_name)
    else:
        print("Invalid number of sides. Please enter a valid number.")

if __name__ == "__main__":
    main()

