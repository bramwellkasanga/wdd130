# tire_volume.py
# This program asks the user for tire dimensions, calculates the approximate
# volume of the tire in liters, and then records the data in a text file.

import math
from datetime import datetime

# Get input from the user
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate the volume of the tire
volume = (math.pi * width**2 * aspect_ratio *
         (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Display the result
print(f"The approximate volume is {volume:.2f} liters")

# Get the current date (year-month-day)
current_date = datetime.now().strftime("%Y-%m-%d")

# Save the data to a file
with open("volumes.txt", "at") as file:
    print(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}", file=file)