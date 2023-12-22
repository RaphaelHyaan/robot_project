from roboticstoolbox import DHRobot, RevoluteMDH, PrismaticMDH
from math import pi
from sympy import symbols
from sympy import Matrix, latex, N
import numpy as np


q = symbols(['q1', 'q2', 'q3','q4', 'q5', 'q6'])

# 创建连杆
L1 = PrismaticMDH(theta=0, a=0, alpha=0, offset=20, qlim=[0, 30])
L2 = PrismaticMDH(theta=pi/2, a=0, alpha=pi/2, offset=10, qlim=[0, 20])
L3 = RevoluteMDH(d=10, a=0, alpha=-pi/2, qlim=[-pi, pi])
L4 = RevoluteMDH(d=0, a=5, alpha=pi/2, offset=pi/2, qlim=[-pi, pi])
L5 = RevoluteMDH(d=0, a=5, alpha=0, offset=pi/2, qlim=[-pi, pi])
L6 = RevoluteMDH(d=0, a=5, alpha=0, offset=0, qlim=[-pi, pi])
# 创建机器人
robot = DHRobot([L1, L2, L3, L4, L5, L6], name='my_robot')

# 计算速度雅可比矩阵
q_values = [0, 0, 0, 0, 0, 0]
# Jv = robot.jacobe(q_values)  # 雅可比矩阵
Jv = robot.jacob0(q_values)  # 雅可比矩阵
# # 将速度雅可比矩阵Jv转换为Matrix对象

# Jv_matrix = Matrix(Jv)

# # 将Matrix对象中的小数保留两位
# Jv_matrix_rounded = Jv_matrix.applyfunc(lambda x: N(x, 2))

# # 将Matrix对象转换为LaTeX格式的公式

# latex_eq = latex(Jv_matrix_rounded)



# # 打印结果
# print("线速度雅可比矩阵：")
# # # 将LaTeX格式的公式保存到txt文件
# # with open("jv_equation_r.txt", "w") as file:
# #     file.write(latex_eq)

# # print("已将LaTeX格式的公式保存到jv_equation.txt文件中。")

# print(latex_eq)


# 将Jv转换为NumPy数组
Jv_np = np.array(Jv).astype(float)

# 计算速度雅可比矩阵的秩
rank = np.linalg.matrix_rank(Jv_np)

if rank < min(Jv_np.shape):
    print("机器人存在奇异点。")
else:
    print("机器人没有奇异点。")