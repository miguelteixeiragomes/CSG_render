from Vector import Vector
from Vectors import Vectors
import numpy as np

v1 = Vector(np.random.random(), np.random.random(), np.random.random())
v2 = Vector(np.random.random(3))
v3 = Vector(list(np.random.random(3)))
v4 = Vector(tuple(np.random.random(3)))

vs1 = Vectors(np.random.random((10, 10, 3)))
vs2 = Vectors(list(np.random.random((10, 10, 3))))
vs3 = Vectors(tuple(np.random.random((10, 10, 3))))

print "v1: %s = (%s, %s, %s)" % (v1, v1[0], v1[1], v1[2])
print "v2: %s = (%s, %s, %s)" % (v2, v2[-3], v2[-2], v2[-1])
print "add:", np.allclose( (vs1 + v1).vec , np.concatenate((vs1.vec[0] + v1[0] , vs1.vec[1] + v1[1] , vs1.vec[2] + v1[2])) )
print "mul:", np.allclose(vs1 * v1 , vs1.vec[0]*v1[0] + vs1.vec[1]*v1[1] + vs1.vec[2]*v1[2])