
import graphics.rectangle
import graphics.circle


from graphics.three_d_graphics import cuboid

from graphics.three_d_graphics.sphere import *


l, b = 5, 3
print("Rectangle Area:", graphics.rectangle.area(l, b))
print("Rectangle Perimeter:", graphics.rectangle.perimeter(l, b))


r = 4
print("\nCircle Area:", graphics.circle.area(r))
print("Circle Perimeter:", graphics.circle.perimeter(r))


print("\nCuboid Surface Area:", cuboid.surface_area(2, 3, 4))
print("Cuboid Perimeter:", cuboid.perimeter(2, 3, 4))


print("\nSphere Surface Area:", surface_area(5))
print("Sphere Perimeter (Great Circle Circumference):", perimeter(5))
