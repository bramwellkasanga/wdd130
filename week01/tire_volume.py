# tire_volume.py
# This program calculates the volume of a tire based on user input
# and logs the results (date, width, aspect ratio, diameter, volume)
# to a file named volumes.txt.

import math
from datetime import datetime

# Get input from the user
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate the volume
volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Display result
print(f"The approximate volume is {volume:.2f} liters")

# Get current date (only date, no time)
current_date_and_time = datetime.now()
current_date = f"{current_date_and_time:%Y-%m-%d}"

# Append results to volumes.txt
with open("volumes.txt", "at") as volumes_file:
    print(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}", file=volumes_file)