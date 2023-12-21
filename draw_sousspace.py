import numpy as np
import numpy as np
import matplotlib.pyplot as plt

N = 10
alpha = np.linspace(-np.pi,np.pi,N)
beta = np.linspace(-3,3,N)
gamma = np.linspace(-3,3,N)
epsilon = np.linspace(-3,3,N)
one = np.ones(N)
zero = np.zeros(N)

def foi(A,B):
    '''
    A:(4,4,x)
    B:(4,4,x)
    '''
    C = np.zeros((4,4,np.shape(A)[2]*np.shape(B)[2]))
    k = 0
    for i in range(np.shape(A)[2]):
        for j in range(np.shape(B)[2]):
            C[:,:,k] = np.dot(A[:,:,i],B[:,:,j])
            k+=1
    return C

T_23 = np.array([[np.cos(alpha), -np.sin(alpha), zero, zero],
    [zero, zero, one, 10*one],
    [-np.sin(alpha), -np.cos(alpha), 0*one, 0*one],
    [0*one, 0*one, 0*one, 1*one]])

T_34 = np.array([[-np.sin(beta), -np.cos(beta), 0*one, 5*one],
    [0*one, 0*one, -1*one, 0*one],
    [np.cos(beta), -np.sin(beta), 0*one, 0*one],
    [0*one, 0*one, 0*one, 1*one]])

T_45 = np.array([[-np.sin(gamma), -np.cos(gamma), 0*one, 5*one],
    [np.cos(gamma), -np.sin(gamma), 0*one, 0*one],
    [0*one, 0*one, 1*one, 0*one],
    [0*one, 0*one, 0*one, 1*one]])

T_56 = np.array([[np.cos(epsilon), -np.sin(epsilon), 0*one, 5*one],
    [np.sin(epsilon), np.cos(epsilon), 0*one, 0*one],
    [0*one, 0*one, 1*one, 0*one],
    [0*one, 0*one, 0*one, 1*one]])

T_26 = foi(foi(T_23,T_34),foi(T_45,T_56))
print()

x = np.linspace(0,30,N)
y = np.linspace(0,20,N)
in_points = np.zeros((4,N*N))
k = 0
for i in range(N):
    for j in range(N):
        in_points[0,k] = x[i]
        in_points[1,k] = y[j]
        in_points[3,k] = 1
        k+=1

out_points = np.zeros((4,N*N*N*N*N*N))
i = 0
for p in in_points.T:
    for  t in T_26.T:
        out_points[:,i] = np.dot(t,p)
        i+=1
print(np.max(out_points))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(out_points[0,:],out_points[1,:],out_points[2,:],c='r',marker='o', alpha=0.5, s=0.1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
print()