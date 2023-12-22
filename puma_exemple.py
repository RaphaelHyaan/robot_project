import roboticstoolbox as rtb
import numpy as np
from sympy import pi
# 创建Puma 560机器人的模型
puma = rtb.models.DH.Puma560()

# 绘制机器人的结构
# puma.plot([0,0,0,0,0,0],block=True)

# q = np.array([20, 10, pi/3, pi/3, pi/3, pi/3])  # 关节位置
q = np.zeros(6)

qd = np.array([0, 0, 0, 0, 0, 0])  # 关节速度
# qd = np.ones(6)
qdd = np.zeros(6)  # 关节加速度
# qdd = np.ones(6)



print(puma.accel(q, qd, qdd))