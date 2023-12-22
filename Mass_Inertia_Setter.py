from sympy import pi
from roboticstoolbox import DHRobot, PrismaticMDH, RevoluteMDH
# from roboticstoolbox import Dynamics
import numpy as np

# 创建连杆
L1 = PrismaticMDH(theta=0, a=0, alpha=0, offset=20, qlim=[0, 30])
L2 = PrismaticMDH(theta=pi/2, a=0, alpha=pi/2, offset=10, qlim=[0, 20])
L3 = RevoluteMDH(d=10, a=0, alpha=-pi/2, qlim=[-pi, pi])
L4 = RevoluteMDH(d=0, a=5, alpha=pi/2, offset=pi/2, qlim=[-pi, pi])
L5 = RevoluteMDH(d=0, a=5, alpha=0, offset=pi/2, qlim=[-pi, pi])
L6 = RevoluteMDH(d=0, a=5, alpha=pi/2, offset=0, qlim=[-pi, pi])

# 设置连杆的质量和惯性参数
L1.m = 23.38782
L1.Ixx = 6.425149
L1.Ixy = -2.20E-16
L1.Ixz = 1.02E-16
L1.Iyy = 1.987009
L1.Iyz = 5.62E-10
L1.Izz = 4.444118

L2.m = 9.205307
L2.Ixx = 0.470912
L2.Ixy = -9.67E-19
L2.Ixz = 2.85E-19
L2.Iyy = 0.012207
L2.Iyz = -7.39E-17
L2.Izz = 0.466974

L3.m = 1.204045
L3.Ixx = 0.000393
L3.Ixy = 4.69E-18
L3.Ixz = 1.27E-08
L3.Iyy = 0.172653
L3.Iyz = -2.23E-19
L3.Izz = 0.17265

L4.m = 0.122888
L4.Ixx = 8.09E-05
L4.Ixy = -5.39E-13
L4.Ixz = -9.25E-20
L4.Iyy = 7.28E-05
L4.Iyz = 3.22E-20
L4.Izz = 7.17E-05

L5.m = 1.139717
L5.Ixx = 0.000433
L5.Ixy = -2.97E-05
L5.Ixz = 3.49E-09
L5.Iyy = 0.029837
L5.Iyz = -1.09E-09
L5.Izz = 0.029969

L6.m = 0.580515
L6.Ixx = 0.012522
L6.Ixy = -2.17E-19
L6.Ixz = -5.60E-17
L6.Iyy = 0.012507
L6.Iyz = -6.07E-17
L6.Izz = 0.000275


# 创建机器人
robot = DHRobot([L1, L2, L3, L4, L5, L6], name='my_robot')

# 定义关节状态（位置、速度和加速度）
# q = np.array([20, 10, pi/3, pi/3, pi/3, pi/3])  # 关节位置
q = np.zeros(6)
qd = np.array([0, 0, 0, 0, 0, 0])  # 关节速度
qdd = np.array([1, 1, 1, 1, 1, 1])  # 关节加速度

# 计算关节力和力矩
tau = robot.rne(q, qd, qdd)

print(tau)