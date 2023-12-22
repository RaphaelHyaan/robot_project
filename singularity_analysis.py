from sympy import symbols, Eq, solve, Matrix
from roboticstoolbox import PrismaticMDH, RevoluteMDH, DHRobot
from math import pi


# 定义符号变量
q = symbols(['q1', 'q2', 'q3', 'q4', 'q5', 'q6'])

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
Jv = robot.jacobe(q)  # 线速度雅可比矩阵带入数值q = [0,0,0,0,0,0]

# 将NumPy数组转换为SymPy矩阵
Jv_sym = Matrix(Jv)

# 计算速度雅可比矩阵的行列式
det_Jv = Jv_sym.det()

# 解方程det_Jv = 0，找到奇异点的配置
solutions = solve(det_Jv, q)

print("奇异点的配置:")
for sol in solutions:
    print(sol)