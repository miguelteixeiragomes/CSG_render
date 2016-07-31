from Vector import Vector
from Vectors import Vectors
import numpy as np

v1 = Vector(np.random.random(), np.random.random(), np.random.random())
v2 = Vector(np.random.random(3))
v3 = Vector(list(np.random.random(3)))
v4 = Vector(tuple(np.random.random(3)))

SHAPE = [11, 12, 13, 14, 15]
vs1 = Vectors(np.random.random(SHAPE + [3]))
vs2 = Vectors(list(np.random.random(SHAPE + [3])))
vs3 = Vectors(tuple(np.random.random(SHAPE + [3])))


a = np.zeros([3] + SHAPE)
a[0] = vs1.vec[0] + v1[0]
a[1] = vs1.vec[1] + v1[1]
a[2] = vs1.vec[2] + v1[2]

b = np.zeros([3] + SHAPE)
b[0] = vs1.vec[0] + vs2.vec[0]
b[1] = vs1.vec[1] + vs2.vec[1]
b[2] = vs1.vec[2] + vs2.vec[2]


print "       V1 + V2:", np.allclose(np.array([(v1 + v2).x, (v1 + v2).y, (v1 + v2).z]), np.array([v1.x + v2.x, v1.y + v2.y, v1.z + v2.z]))
print "     Vs1 + Vs2:", np.allclose((vs1 + vs2).vec, b)
print "      Vs1 + V1:", np.allclose((vs1 + v1).vec, a)
print "      V1 + Vs1:", np.allclose((v1 + vs1).vec, a)

print "       V1 * V2:", np.allclose(np.array([v1*v2]), np.array([v1.x*v2.x + v1.y*v2.y + v1.z*v2.z]))
print "      V1 * 7.0:", np.allclose(np.array([(v1*7.).x, (v1*7.).y, (v1*7.).z]), np.array([v1.x*7., v1.y*7., v1.z*7.]))
print "      7.0 * V1:", np.allclose(np.array([(7.*v1).x, (7.*v1).y, (7.*v1).z]), np.array([v1.x*7., v1.y*7., v1.z*7.]))
print "     Vs1 * Vs2:", np.allclose(vs1*vs2, vs1.vec[0]*vs2.vec[0] + vs1.vec[1]*vs2.vec[1] + vs1.vec[2]*vs2.vec[2])
print "     Vs1 * 7.0:", np.allclose((vs1*7.0).vec, vs1.vec*7.0)
print "     7.0 * Vs1:", np.allclose((7.0*vs1).vec, vs1.vec*7.0)
print "      Vs1 * V1:", np.allclose(vs1 * v1, vs1.vec[0]*v1[0] + vs1.vec[1]*v1[1] + vs1.vec[2]*v1[2])
print "      V1 * Vs1:", np.allclose(v1 * vs1, vs1.vec[0]*v1[0] + vs1.vec[1]*v1[1] + vs1.vec[2]*v1[2])

print "       abs(V1):", np.allclose(np.array([abs(v1)]), np.array([np.sqrt(v1.x**2 + v1.y**2 + v1.z**2)]))
print "      abs(Vs1):", np.allclose(abs(vs1), np.sqrt(vs1.vec[0]**2 + vs1.vec[1]**2 + vs1.vec[2]**2))

print "  V1.angle(V2):", np.allclose(np.array([v1 ^ v2]), np.array([np.arccos((v1 * v2) / (abs(v1) * abs(v2)))]))
print "Vs1.angle(Vs2):", np.allclose(vs1 ^ vs2, np.arccos((vs1 * vs2) / np.sqrt(vs1.abs2() * vs2.abs2())))
print " Vs1.angle(V1):", np.allclose(vs1 ^ v1, np.arccos((vs1 * v1) / np.sqrt(vs1.abs2() * v1.abs2())))
print " V1.angle(Vs1):", np.allclose(v1 ^ vs1, np.arccos((vs1 * v1) / np.sqrt(vs1.abs2() * v1.abs2())))

print "      V1 == V1:", (v1 == v1) == True
print "      V1 == V2:", (v1 == v2) == False
print "      V1 != V1:", (v1 != v1) == False
print "      V1 != V2:", (v1 != v2) == True
print "    Vs1 == Vs1:", np.sum(vs1 == vs1) == reduce(lambda x, y: x*y, SHAPE, 1)
print "    Vs1 == Vs2:", np.sum(vs1 == vs2) == 0
print "    Vs1 != Vs1:", np.sum(vs1 != vs1) == 0
print "    Vs1 != Vs2:", np.sum(vs1 != vs2) == reduce(lambda x, y: x*y, SHAPE, 1)
