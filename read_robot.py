from math import pi
from roboticstoolbox import DHRobot, RevoluteMDH, PrismaticMDH
import roboticstoolbox as rtb
import numpy as np
import time
import matplotlib.pyplot as plt

def xplot(
    x,
    y=None,
    wrist=False,
    unwrap=False,
    block=False,
    labels=None,
    loc=None,
    grid=True,
    stack=False,
    **kwargs,
):
    """
    Plot trajectory data

    :param x: trajectory, one row per timestep
    :type x: ndarray(m,n)
    :param t: time vector, optional
    :type t: numpy ndarray, shape=(M,)
    :param wrist: distinguish arm and wrist joints with line styles
    :type wrist: bool
    :param unwrap: unwrap joint angles so that they smoothly increase or
        decrease when they pass through :math:`\pm \pi`
    :type unwrap: bool
    :param block: block until the plot is closed
    :type block: bool
    :param labels: legend labels
    :type labels: list of str, or single string with space separated labels
    :param kwargs: options passed to pyplot.plot
    :param loc: legend location as per pyplot.legend
    :type loc: str

    This is a convenience function to plot trajectories, where each row represents one time step.

    - ``xplot(q)`` plots the joint angles versus row number.  If N==6 a
      conventional 6-axis robot is assumed, and the first three joints are
      shown as solid lines, the last three joints (wrist) are shown as dashed
      lines. A legend is also displayed.

    - ``xplot(t, q)`` as above but displays the joint angle trajectory versus
      time given the time vector T (Mx1).

    Example::

        >>> qplot(q, x, labels='x y z')

    :seealso: :func:`jtraj`, :func:`numpy.unwrap`
    """
    if y is None:
        q = x
        t = np.arange(0, q.shape[0])
    else:
        t = x
        q = y

    if q.ndim == 1:
        # if 1D, make it Nx1
        q = q[:, np.newaxis]

    if t.ndim != 1 or q.shape[0] != t.shape[0]:
        raise ValueError("dimensions of arguments are not consistent")

    if unwrap:
        q = np.unwrap(q, axis=0)

    n = q.shape[1]

    if labels is None:
        labels = [f"q{i}" for i in range(n)]
    elif isinstance(labels, str):
        labels = labels.split(" ")
    elif not isinstance(labels, (tuple, list)):
        raise TypeError("wrong type for labels")

    fig, ax = plt.subplots()

    if stack:
        for i in range(n):
            ax = plt.subplot(n, 1, i + 1)

            plt.plot(t, q[:, i], **kwargs)

            plt.grid(grid)
            ax.set_ylabel(labels[i])
            ax.set_xlim(t[0], t[-1])

        ax.set_xlabel("Time (s)")

    else:
        if n == 6 and wrist:
            plt.plot(t, q[:, 0:3], **kwargs)
            plt.plot(t, q[:, 3:6], "--", **kwargs)
        else:
            plt.plot(t, q, **kwargs)

        ax.legend(labels, loc=loc)

        plt.grid(grid)
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Joint coordinates (rad,m)")
        # ax.set_xlim(t[0], t[-1])  fails with RVC3 Sec 3.3.3

    plt.show(block=block)

    return fig.get_axes()


# 创建连杆
L1 = PrismaticMDH(theta=0, a=0, alpha=0, offset=20, qlim=[0, 30])
L2 = PrismaticMDH(theta=pi/2, a=0, alpha=pi/2, offset=10, qlim=[0, 20])
L3 = RevoluteMDH(d=10, a=0, alpha=-pi/2, qlim=[-pi, pi])
L4 = RevoluteMDH(d=0, a=5, alpha=pi/2, offset=pi/2, qlim=[-pi, pi])
L5 = RevoluteMDH(d=0, a=5, alpha=0, offset=pi/2, qlim=[-pi, pi])
L6 = RevoluteMDH(d=0, a=5, alpha=0, offset=0, qlim=[-pi, pi])

# 创建机器人
robot = DHRobot([L1, L2, L3, L4, L5, L6], name='my_robot')


# print(robot.mdh)
# q0 = [0, 0, 0, 0, 0, 0]
# robot.plot(q=q0,block = True)
q = [0, 0, pi/6, pi/6, 0, pi/6]
# # q = [0, 0, pi/6, 4*pi/6, pi, 4*pi/6]
# # print(robot.A((0,0),q=q))
# # print(robot.A((1,1),q=q))
# print(robot.A((2,2),q=q))
# print(robot.A((3,3),q=q))
# print(robot.A((4,4),q=q))
# print(robot.A((5,5),q=q))
# # print(robot.A((2,5),q=q))
T = robot.fkine(q)
begin = time.time()
# print(robot.ets().ikine_LM(T,slimit = 10000))
# print(robot.ets().ikine_NR(T,slimit = 100000))
print(robot.ets().ikine_QP(T,slimit = 10000))
end = time.time()
print(end-begin)
q2=[1.017, 3.04, 0.5236, -0.9829, 1.173, 0.8575]
robot.plot(q=q,block = True)
robot.plot(q=q2,block = True)
print()