import numpy as np
import numpy as np
import matplotlib.pyplot as plt

alpha = np.ones((1))*np.pi/6
beta = np.ones((1))*np.pi/6
gamma = np.ones((1))*np.pi/6
epsilon = np.ones((1))*np.pi/6
one = np.ones((1))*1
zero = np.ones((1))*0
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
print(T_23[:,:,0],'\n')
T_34 = np.array([[-np.sin(beta), -np.cos(beta), 0*one, 5*one],
    [0*one, 0*one, -1*one, 0*one],
    [np.cos(beta), -np.sin(beta), 0*one, 0*one],
    [0*one, 0*one, 0*one, 1*one]])
print(T_34[:,:,0],'\n')
T_45 = np.array([[-np.sin(gamma), -np.cos(gamma), 0*one, 5*one],
    [np.cos(gamma), -np.sin(gamma), 0*one, 0*one],
    [0*one, 0*one, 1*one, 0*one],
    [0*one, 0*one, 0*one, 1*one]])
print(T_45[:,:,0],'\n')
T_56 = np.array([[np.cos(epsilon), -np.sin(epsilon), 0*one, 5*one],
    [np.sin(epsilon), np.cos(epsilon), 0*one, 0*one],
    [0*one, 0*one, 1*one, 0*one],
    [0*one, 0*one, 0*one, 1*one]])
print(T_56[:,:,0],'\n')
T_26 = foi(foi(T_23,T_34),foi(T_45,T_56))

# T_24 = np.einsum('ijk,jlk->ilk',np.einsum('ijk,jlk->ilk',np.einsum('ijk,jlk->ilk',T_23,T_34),T_45),T_56)
print(T_26[:,:,0])
print()