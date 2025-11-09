import numpy as np
import numpy.linalg as alg
l_part=np.array([[-2,-8.5,-3.4,3.5],[0,2.4,0,8.2],[2.5,1.6,2.1,3],[0.3,-0.4,-4.8,4.6]])
r_part=np.array([-1.88,-3.28,-0.5,-2.83])
if alg.det(l_part)==0:
    print('Вырожденная матрица,деление на 0')
else:
    inv_lpart=alg.inv(l_part)
    x=np.dot(inv_lpart,r_part)
    x=np.round(x,1)
print("Вектор решения: ",x)