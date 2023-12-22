"""
rotation_calculation.py

This program calculates the angular velocity relationship between two coordinate frames using rotation matrices and symbolic variables.
"""

from sympy import symbols, cos, sin, Matrix

# Define symbolic variables
alpha, theta = symbols('alpha theta')

# Define the rotation matrix R_2^3
R_2_3 = Matrix([
    [cos(alpha), -sin(alpha), 0],
    [0, 0, 1],
    [-sin(alpha), -cos(alpha), 0]
])

# Define the rotation axis vector Z_i+1^i
Z_i_1_i = Matrix([
    [0],
    [1],
    [0]
])

# Define the angular velocity variables
omega_i = Matrix([
    [symbols('omega_i_1')],
    [symbols('omega_i_2')],
    [symbols('omega_i_3')]
])

omega_i_1 = Matrix([
    [symbols('omega_i_1_1')],
    [symbols('omega_i_1_2')],
    [symbols('omega_i_1_3')]
])

# Calculate the angular velocity relationship
omega_i_1_i = R_2_3 * omega_i + theta * Z_i_1_i

# Print the result
print("omega_i+1^i =")
print(omega_i_1_i)
