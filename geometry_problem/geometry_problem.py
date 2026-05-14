'''
The slant height and lateral edge of a regular triangular pyramid are
Both 25 cm. The apothem of the pyramid is equal to the radius of the
Base of the cone. Calculate the area (in square centimetres) of the
Lateral surface of the pyramid, given that the area of the lateral
Surface of the cone is 500 pi cm²
'''

# Solution
# Generating line of a cone = edge of a regular triangular pyramid.
# The pyramid is regular and triangular, so its lateral edges are
# Equal in length, and its base is a regular triangle.
# Apothem = radius of the base of the cone.
# The lateral surface area of the cone = 500π cm² =>

# Import math
import math

# Search radius
radius = (500 * math.pi) / (25 * math.pi)

# Search half of the base of the pyramid
half_of_the_base = math.sqrt((25 ** 2 - 20 ** 2))

# Search all base
base = half_of_the_base * 2

# Search the lateral surface area of a pyramid
lateral_area_pyramid = (base * 3 * radius) / 2
print(f"The lateral surface area of a pyramid equal {int(round(lateral_area_pyramid, 1))}")

# Interactive variation of this task:

def get_geometry_data():
    while True:
        try:
            generating_line = float(input("Enter the slant height of the cone (L): "))
            side_edge = float(input("Enter the lateral edge of the pyramid (b): "))
            cone_area_coefficient = float(input("Enter the cone lateral area coefficient (before pi): "))
            lateral_surface_cone = cone_area_coefficient * math.pi
        except ValueError:
            print("Please, enter a correct value")
            continue

        if generating_line <= 0 or side_edge <= 0 or lateral_surface_cone <= 0:
            print("Please, write a correct value")
            continue

        radius_of_cone = lateral_surface_cone / (math.pi * generating_line)

        apothem = radius_of_cone

        if side_edge <= apothem:
            print(f"Geometry error: Side edge ({side_edge}) must be greater than the calculated apothem ({apothem:.2f}).")
            continue

        return side_edge, apothem


def calculate_pyramid_lateral_area(side_edge, apothem):
    half_pyramid_base = math.sqrt(side_edge ** 2 - apothem ** 2)

    base_side = half_pyramid_base * 2

    perimeter = base_side * 3

    lateral_area = (perimeter * apothem) / 2
    return lateral_area

edge_val, apothem_val = get_geometry_data()
final_area = calculate_pyramid_lateral_area(edge_val, apothem_val)

print("\n--- Geometric Results ---")
print(f"Calculated Apothem (Radius): {int(round(apothem_val))} cm")
print(f"The lateral area of the pyramid is: {int(round(final_area))} cm²")


