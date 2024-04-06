import math

PI = 3.14
ONE_HALF = 1 / 2

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

def test():
    print(rectangular_prism_sa(5, 5, 5))
    print(cube_sa(5))
    print(sphere_sa(5))
    print(cone_sa(5, 5))
    print(cylinder_sa(5, 5))
    print(pyramid_sa("rect", 5, 5, 5))
    print(ellipsoid_sa(5, 5, 5))
    print(icosahedron_sa(5))
    print(octahedron_sa(5))
    print(hexagonal_prism_sa(5, 5))
    print(dodecahedron_sa(5))
    print(pentagonal_prism_sa(5, 5))
    print(torus_area(10, 5))
    print(tetrahedron_sa(5))
    
if __name__ == "__main__":
    test()