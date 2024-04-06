import math

PI = 3.14
ONE_THIRD = 1 / 3
FIVE_SIXTHS = 5 / 6
ONE_FOURTH = 1 / 4
TWO_THIRDS = 2 / 3
SQRT5 = math.sqrt(5)
SQRT3 = math.sqrt(3)

def rectangular_prism_sa(length, width, height):
    rectangular_prism_sa_final = 2 * (width * length + height * length + height * width)
    return rectangular_prism_sa_final

def cube_sa(side):
    final_cube_sa = 6 * (side ** 2)
    return final_cube_sa

def sphere_sa(radius):
    sphere_sa_final = 4 * PI * (radius ** 2)
    return sphere_sa_final

def cone_sa(radius, height):
    calculating = height ** 2
    calculating1 = radius ** 2
    calculating2 = math.sqrt(calculating + calculating1)
    cone_sa_final = (PI * radius) * (radius + calculating2)
    return cone_sa_final

def cylinder_sa(radius, height):
    cylinder_sa_final = 2 * PI * radius * height + 2 * PI * (radius ** 2)
    return cylinder_sa_final

def pyramid_sa(type, length, width, height):
    if type.lower() == "rectangular" or type.lower() == "rectangle" or type.lower() == "square" or type.lower() == "rect" or type.lower() == "squ":
        calculating = (width / 2) ** 2
        calculating1 = calculating + (height ** 2)
        calculating2 = math.sqrt(calculating1)
        calculating3 = ((length / 2) ** 2) + (height ** 2)
        calculating4 = math.sqrt(calculating3)
        pyramid_sa_final = (length * width) + length * calculating2 + (width * calculating4)
        return pyramid_sa_final

def ellipsoid_sa(a_axis, b_axis, c_axis):
    calculating = ((((a_axis * b_axis) ** 1.6) + ((a_axis * c_axis) ** 1.6) + ((b_axis * c_axis) ** 1.6)) / 3) ** (1 / 1.6)
    ellipsoid_sa_final = 4 * PI * calculating
    return ellipsoid_sa_final

def icosahedron_sa(edge):
    sqrt3 = math.sqrt(3)
    icosahedron_sa_final = 5 * sqrt3 * (edge ** 2)
    return icosahedron_sa_final

def octahedron_sa(edge):
    octahedron_sa_final = 2 * math.sqrt(3) * (edge ** 2)
    return octahedron_sa_final

def hexagonal_prism_sa(base_edge, height):
    hexagonal_prism_sa_final = 6 * base_edge * height + 3 * math.sqrt(3) * (base_edge ** 2)
    return hexagonal_prism_sa_final

def dodecahedron_sa(edge):
    dodecahedron_sa_final = (3 * math.sqrt(25 + 10 * math.sqrt(5)) * (edge ** 2))
    return dodecahedron_sa_final

def pentagonal_prism_sa(base_edge, height):
    pentagonal_prism_sa_final = 5 * base_edge * height + ONE_HALF * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (base_edge ** 2)
    return pentagonal_prism_sa_final

def torus_area(Major_radius, Minor_radius):
    torus_area_final = (2 * PI * Major_radius) * (2 * PI * Minor_radius)
    return torus_area_final

def tetrahedron_sa(edge):
    tetrahedron_sa_final = math.sqrt(3) * (edge ** 2)
    return tetrahedron_sa_final

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

def rect_prism_vol(length, width, height):
    rect_prism_final = length * width * height
    return rect_prism_final

def cube_vol(length, width, height):
    cube_final = length * width * height
    return cube_final

def sphere_vol(radius):
    r3 = (radius * radius) * radius
    sphere_final = (FOUR_THIRDS * PI) * r3
    return sphere_final

def cylinder_vol(radius, height):
    pi_r2 = (radius * radius) * PI  
    cylinder_final = pi_r2 * height
    return cylinder_final

def triangular_prism_vol(length_of_triangle, length, height):
    tri_normal = (length_of_triangle * height) * length
    tri_prism_final = tri_normal / 2
    return tri_prism_final

def tri_prism_vol(length_of_triangle, length, height):
    tri_normal = (length_of_triangle * height) * length
    tri_prism_final = tri_normal / 2
    return tri_prism_final

def cone_vol(radius, height):
    r2 = radius * radius
    cone_normal = (PI * r2) * height
    cone_final = cone_normal / 3
    return cone_final

def pyramid_vol(type, length, width, height):
    try:
        if type.lower() == "triangle" or type.lower() == "tri" or type.lower() == "triangular":
            pyramid_base = length * width
            pyramid_base1 = pyramid_base / 2
            pyramid_normal = pyramid_base1 * height
            pyramid_final = pyramid_normal / 3
            return pyramid_final
        elif type.lower() == "square" or type.lower() == "squ" or type.lower() == "rectangular" or type.lower() == "rectangle" or type.lower() == "rect":
            pyramid_base = length * width
            pyramid_normal = pyramid_base * height
            pyramid_final = pyramid_normal / 3
            return pyramid_final
    except:
        print("ERROR")

def icosahedron_vol(edge):
    calculating1 = 5 * (3 + SQRT5)
    icosahedron_final = (calculating1 / 12) * (edge ** 3)
    return icosahedron_final

def octahedron_vol(edge):
    sqrt2 = math.sqrt(2)
    octahedron_final = (sqrt2 / 3) * (edge ** 3)
    return octahedron_final

def hexagonal_prism_vol(base_edge, height):
    calculating = (3 * SQRT3) / 2
    hexagonal_prism_final = calculating * (base_edge ** 2) * height
    return hexagonal_prism_final

def hex_prism_vol(base_edge, height):
    calculating = (3 * SQRT3) / 2
    hexagonal_prism_final = calculating * (base_edge ** 2) * height
    return hexagonal_prism_final

def dodecahedron_vol(edge):
    calculating = (15 + 7 * SQRT5) / 4
    dodecahedron_final = calculating * (edge ** 3)
    return dodecahedron_final

def pentagonal_prism_vol(base_edge, height):
    calculating = 5 * (5 + 2 * SQRT5)
    calculating1 = math.sqrt(calculating)
    calculating2 = ONE_FOURTH * calculating1
    pentagonal_prism_final = calculating2 * (base_edge ** 2) * height
    return pentagonal_prism_final

def torus_vol(major_radius, minor_radius):
    if minor_radius >= major_radius:
        print("Error: major radius must be bigger than the minor radius")
    else:
        torus_final = (PI * (minor_radius ** 2)) * (2 * PI * major_radius)
        return torus_final

def ellipsoid_vol(a_axis, b_axis, c_axis):
    ellipsoid_final = FOUR_THIRDS * PI * a_axis * b_axis * c_axis
    return ellipsoid_final

def tetrahedron_vol(edge):
    sqrt2 = math.sqrt(2)
    tetrahedron_final = (edge ** 3) / (6 * sqrt2)
    return tetrahedron_final
