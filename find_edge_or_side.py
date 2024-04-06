import math

PI = 3.14
ONE_THIRD = 1 / 3
FIVE_SIXTHS = 5 / 6
ONE_FOURTH = 1 / 4
TWO_THIRDS = 2 / 3

def rectangular_prism_find_length(width, height, volume):
  rectangular_prism_find_length_final = volume / (width * height)
  return rectangular_prism_find_length_final

def rectangular_prism_find_width(length, height, volume):
  rectangular_prism_find_width_final = volume / (length * height)
  return rectangular_prism_find_width_final

def rectangular_prism_find_height(length, width, volume):
  rectangular_prism_find_height_final = volume / (length * width)
  return rectangular_prism_find_height_final

def sphere_find_radius(volume):
  sphere_find_radius_final = (3 * (volume / (4 * PI))) ** ONE_THIRD
  return sphere_find_radius_final

def sphere_find_diameter(radius):
  sphere_find_diameter_final = 2 * radius
  return sphere_find_diameter_final

def cone_find_height(radius, volume):
  cone_find_height_final = 3 * (volume / (PI * (radius ** 2)))
  return cone_find_height_final

def cone_find_slant_height(radius, height):
  cone_find_slant_height_final = math.sqrt((radius ** 2) + (height ** 2))
  return cone_find_slant_height_final

def cone_find_lateral_surface(radius, height):
  cone_find_lateral_surface_final = PI * radius * math.sqrt((height ** 2) + (radius ** 2))
  return cone_find_lateral_surface_final

def cone_find_base_area(radius):
  cone_find_base_area_final = PI * (radius ** 2)
  return cone_find_base_area_final

def cone_find_radius(base_area):
  cone_find_radius_final = math.sqrt(base_area / PI)
  return cone_find_radius_final

def cylinder_find_radius(height, volume):
  cylinder_find_radius_final = math.sqrt(volume / (PI * height))
  return cylinder_find_radius_final

def cylinder_find_height(radius, volume):
  cylinder_find_height_final = volume / (PI * (radius ** 2))
  return cylinder_find_height_final

def cylinder_find_lateral_surface(radius, height):
  cylinder_find_lateral_surface_final = 2 * PI * radius * height
  return cylinder_find_lateral_surface_final

def cylinder_find_base_area(radius):
  cylinder_find_base_area_final = PI * (radius ** 2)
  return cylinder_find_base_area_final

def pyramid_find_base_length(width, height, volume):
  pyramid_find_base_length_final = 3 * (volume / (height * width))
  return pyramid_find_base_length_final

def pyramid_find_base_width(length, height, volume):
  pyramid_find_base_width_final = 3 * (volume / (height * length))
  return pyramid_find_base_width_final

def pyramid_find_height(length, width, volume):
  pyramid_find_height_final = 3 * (volume / (length * width))
  return pyramid_find_base_height_final

def pyramid_find_lateral_surface(length, width, height):
  calculating = length * math.sqrt(((width / 2) ** 2) + (height ** 2))
  pyramid_find_lateral_surface_final = calculating + (width * math.sqrt(((length / 2) ** 2) + (height ** 2)))
  return pyramid_find_lateral_surface_final

def ellipsoid_find_a_axis(b_axis, c_axis, volume):
    a_axis = (6 * volume / (math.pi * b_axis * c_axis)) ** (1/3)
    return a_axis

def ellipsoid_find_b_axis(a_axis, c_axis, volume):
  b_axis = (3 * (volume / (4 * math.pi * a_axis * c_axis)))
  return b_axis

def ellipsoid_find_c_axis(a_axis, b_axis, volume):
  c_axis = (3 * (volume / (4 * math.pi * a_axis * b_axis)))
  return c_axis

def icosahedron_find_edge(volume):
  edge = (9 * (volume / 5) - (3 * math.sqrt(5) * (volume / 5))) ** ONE_THIRD
  return edge

def octahedron_find_edge(volume):
  edge = (2 ** FIVE_SIXTHS) * ((3 * (volume / 8)) ** ONE_THIRD)
  return edge

def hexagonal_prism_find_base_edge(height, volume):
  base_edge = ((3 ** ONE_FOURTH) * math.sqrt(2 * (volume / (9 * height))))
  return base_edge

def hexagonal_prism_find_height(base_edge, volume):
  height = (2 * math.sqrt(3) * (volume / (9 * (base_edge ** 2))))
  return height

def hexagonal_prism_find_lateral_surface(base_edge, height):
  lateral_surface = (6 * base_edge * height)
  return lateral_surface

def hexagonal_prism_find_base_area(base_edge):
  base_area = (3 * math.sqrt(3) * ((base_edge ** 2) / 2))
  return base_area

def dodecahedron_find_edge(volume):
  #edge = ((2 ** TWO_THIRDS) * (volume / (15 + math.sqrt(245)) ** (1 / 3)))
  calculating = (2 ** TWO_THIRDS)
  calculating1 = ((volume / (15 + math.sqrt(245))) ** ONE_THIRD)
  edge = calculating * calculating1
  return edge

def torus_find_minor_radius(major_radius, area):
  minor_radius = (area / (4 * (math.pi ** 2) * major_radius))
  return minor_radius

def torus_find_major_radius(minor_radius, area):
  major_radius = (area / (4 * (math.pi ** 2) * minor_radius))
  return major_radius

def tetrahedron_find_edge(volume):
  edge = (math.sqrt(2) * ((3 * volume) ** ONE_THIRD))
  return edge

def tetrahedron_find_height(edge):
  height = (math.sqrt(TWO_THIRDS) * edge)
  return height

def tetrahedron_find_face_area(edge):
  face_area = ((math.sqrt(3) / 4) * (edge ** 2))
  return face_area
