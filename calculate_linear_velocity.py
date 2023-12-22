from sympy import symbols, Matrix

# Define symbolic variables
v2_x, v2_y, v2_z = symbols('v2_x v2_y v2_z')
omega2_x, omega2_y, omega2_z = symbols('omega2_x omega2_y omega2_z')

# Define transformation matrix T_2_3
T_2_3 = Matrix([
    [0],
    [10],
    [0]
])

# Define linear velocity vector v_2
v_2 = Matrix([
    [v2_x],
    [v2_y],
    [v2_z]
])

# Define angular velocity vector omega_2
omega_2 = Matrix([
    [omega2_x],
    [omega2_y],
    [omega2_z]
])

# Calculate linear velocity relationship
v_3 = v_2 + omega_2.cross(T_2_3)

# Print the result
print("v_3 =")
print(v_3)
