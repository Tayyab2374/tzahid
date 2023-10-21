#!/usr/bin/env python
# coding: utf-8

# ### White-Box Testing - Scenario B: Calculating Perimeters and Areas

# In[3]:


from Calculating_Perimeters_and_Areas import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Test function for calculating perimeters
def test_calculate_perimeter():
    # Test a valid square with 4 sides and a valid triangle with 3 sides
    assert calculate_perimeter(4, "Square") == 16.0
    assert calculate_perimeter(3, "Triangle") == 9.0
    # Test a valid pentagon with 5 sides
    assert calculate_perimeter(5, "Pentagon") == 25.0
    # Test an invalid hexagon with 6 sides (not in the function's dictionary)
    assert calculate_perimeter(6, "Hexagon") == "Unknown shape"
    
# Test function for calculating areas
def test_calculate_area():
    # Test a valid square with 4 sides
    assert calculate_area(4, "Square") == 16.0
    # Test a valid hexagon with 6 sides
    assert round(calculate_area(6, "Hexagon"), 2) == 93.53  # Approximate value
    # Test an invalid shape "Unknown" (not in the function's dictionary)
    assert calculate_area(5, "Unknown") == "Unknown shape"

# Run the test functions
test_calculate_perimeter()
test_calculate_area()


# In[7]:


import unittest
from Calculating_Perimeters_and_Areas import *

class TestCalculatingPerimetersAndAreas(unittest.TestCase):

    def test_calculate_perimeter(self):
        # Test cases for valid inputs
        self.assertEqual(calculate_perimeter(4, 5), 20.0)  # Square with side length 5
        self.assertEqual(calculate_perimeter(3, 8), 24.0)  # Triangle with side length 8
        self.assertEqual(calculate_perimeter(5, 6), 30.0)  # Pentagon with side length 6

        # Test cases for invalid inputs
        self.assertIsNone(calculate_perimeter(2, 7))  # Invalid polygon (2 sides)
        self.assertIsNone(calculate_perimeter(10, 4))  # Invalid polygon (10 sides)

    def test_calculate_area(self):
        # Test cases for valid inputs
        self.assertAlmostEqual(calculate_area(4, 5), 25.0, places=2)  # Square with side length 5
        self.assertAlmostEqual(calculate_area(3, 8), 27.71, places=2)  # Triangle with side length 8
        self.assertAlmostEqual(calculate_area(5, 6), 61.88, places=2)  # Pentagon with side length 6

        # Test cases for invalid inputs
        self.assertIsNone(calculate_area(2, 7))  # Invalid polygon (2 sides)
        self.assertIsNone(calculate_area(10, 4))  # Invalid polygon (10 sides)

if __name__ == '__main__':
    unittest.main()


# In[ ]:




