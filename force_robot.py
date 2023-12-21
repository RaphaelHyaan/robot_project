# import rospy
from math import pi
from numpy import array
# from scipy.spatial.transform import Rotation
from spatialmath import SE3
# from spatialmath.base import tr2rpy
# from spatialmath.base.transforms3d import trchain

# 导入Robotics Toolbox
from roboticstoolbox import DHRobot, RevoluteMDH, PrismaticMDH

# 定义每个关节的DH参数
# L1是一个平移关节，theta=0，a=0，alpha=0，offset=20，qlim=[0, 30]
L1 = PrismaticMDH(theta=0, a=0, alpha=0, offset=20, qlim=[0, 30])
# L2是一个平移关节，theta=pi/2，a=0，alpha=pi/2，offset=10，qlim=[0, 20]
L2 = PrismaticMDH(theta=pi/2, a=0, alpha=pi/2, offset=10, qlim=[0, 20])
# L3是一个旋转关节，d=10，a=0，alpha=-pi/2，qlim=[-pi, pi]
L3 = RevoluteMDH(d=10, a=0, alpha=-pi/2, qlim=[-pi, pi])
# L4是一个旋转关节，d=0，a=5，alpha=pi/2，offset=pi/2，qlim=[-pi, pi]
L4 = RevoluteMDH(d=0, a=5, alpha=pi/2, offset=pi/2, qlim=[-pi, pi])
# L5是一个旋转关节，d=0，a=5，alpha=0，offset=pi/2，qlim=[-pi, pi]
L5 = RevoluteMDH(d=0, a=5, alpha=0, offset=pi/2, qlim=[-pi, pi])
# L6是一个旋转关节，d=0，a=5，alpha=0，offset=0，qlim=[-pi, pi]
L6 = RevoluteMDH(d=0, a=5, alpha=0, offset=0, qlim=[-pi, pi])

# 创建机器人模型
robot = DHRobot([L1, L2, L3, L4, L5, L6], name='my_robot')

# 定义关节角度
q = array([0, 0, 0, 0, 0, 0])

# 执行正向运动学，获取末端执行器位姿
T = robot.ets().fkine(q)

# 执行逆向运动学，获取末端执行器位姿对应的关节角度
desired_pose = SE3.Rx(0.1) * SE3.Ty(0.2) * SE3.Tz(0.3)
# q_ik = robot.ets().ikine(desired_pose)

# 执行逆向动力学，计算给定关节轨迹下的关节力矩
q_traj = array([[0, 0, 0, 0, 0, 0], [pi/4, pi/4, pi/4, pi/4, pi/4, pi/4], [pi/2, pi/2, pi/2, pi/2, pi/2, pi/2]])
qd_traj = array([[0, 0, 0, 0, 0, 0], [0.1, 0.1, 0.1, 0.1, 0.1, 0.1], [0.2, 0.2, 0.2, 0.2, 0.2, 0.2]])
qdd_traj = array([[0, 0, 0, 0, 0, 0], [0.01, 0.01, 0.01, 0.01, 0.01, 0.01], [0.02, 0.02, 0.02, 0.02, 0.02, 0.02]])
tau = robot.rne(q_traj, qd_traj, qdd_traj)

# 打印结果
print("正向运动学结果：")
print(T)
print("")

print("逆向运动学结果：")
# print(q_ik)
print("")

print("逆向动力学结果：")
print(tau)