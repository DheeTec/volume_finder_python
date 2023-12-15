import math

# Function to calculate the volume of a cube
def cube_volume(side_length):
    return side_length ** 3

# Function to calculate the volume of a sphere
def sphere_volume(radius):
    return (4/3) * math.pi * radius ** 3

# Function to calculate the volume of a cylinder
def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height

# Function to calculate the volume of a cone
def cone_volume(radius, height):
    return (1/3) * math.pi * radius ** 2 * height

# Example usage
side_length_cube = 5
radius_sphere = 3
radius_cylinder = 2
height_cylinder = 8
radius_cone = 4
height_cone = 6

# Calculate volumes
volume_cube = cube_volume(side_length_cube)
volume_sphere = sphere_volume(radius_sphere)
volume_cylinder = cylinder_volume(radius_cylinder, height_cylinder)
volume_cone = cone_volume(radius_cone, height_cone)

# Display results
print(f"Volume of Cube: {volume_cube}")
print(f"Volume of Sphere: {volume_sphere}")
print(f"Volume of Cylinder: {volume_cylinder}")
print(f"Volume of Cone: {volume_cone}")
