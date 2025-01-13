import math

PI = math.pi
radius = input("Enter the radius of the cylinder: ")
height = input("Enter the height of the cylinder: ")

cylinder_volume = PI * float(radius) ** 2 * float(height)

print(f"The volume of the cylinder is {cylinder_volume:.2f} cubic units.")