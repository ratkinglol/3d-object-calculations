import math

PI = 3.14
FOUR_THIRDS = 4 / 3
SQRT5 = math.sqrt(5)
SQRT3 = math.sqrt(3)
ONE_FOURTH = 1 / 4

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
    torus_final = (PI * (minor_radius ** 2)) * (2 * PI * major_radius)
    return torus_final

def ellipsoid_vol(a_axis, b_axis, c_axis):
    ellipsoid_final = FOUR_THIRDS * PI * a_axis * b_axis * c_axis
    return ellipsoid_final

def tetrahedron_vol(edge):
    sqrt2 = math.sqrt(2)
    tetrahedron_final = (edge ** 3) / (6 * sqrt2)
    return tetrahedron_final