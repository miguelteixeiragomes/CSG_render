import numpy as np
from Vectors import Vectors


class Vector:
    def __init__(self, *args):
        if len(args) == 3:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]
        elif len(args) == 1:
            try:
                self.x = args[0][0]
                self.y = args[0][1]
                self.z = args[0][2]
            except:
                raise TypeError("The single argument must have __getitem__ method.")
        else:
            raise AttributeError("'Vector' must be initiated with 1 or 3 arguments not %d" % (len(args),))

    def __str__(self):
        return "(%s, %s, %s)" % (str(self.x), str(self.y), str(self.z))

    def __repr__(self):
        return str(self)

    def __getitem__(self, key):
        if key == 0 or key == -3:
            return self.x
        if key == 1 or key == -2:
            return self.y
        if key == 2 or key == -1:
            return self.z
        raise IndexError("Index %d is out of bounds for vector of size 3." % (key,))

    def __eq__(self, vect):
        if isinstance(vect, Vectors):
            vect.vec = np.swapaxes(vect.vec, 0, -1)
            ret = (vect.vec[0] == self.x) & (vect.vec[1] == self.y) & (vect.vec[2] == self.z)
            vect.vec = np.swapaxes(vect.vec, 0, -1)
        return self.x == vect.x and self.y == vect.y and self.z == vect.z

    def __ne__(self, vect):
        if isinstance(vect, Vectors):
            return ~(self == vect)
        return not (self == vect)

    def __pos__(self):
        return Vector(self.x, self.y, self.z)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __add__(self, vect):
        return Vector(self.x + vect.x, self.y + vect.y, self.z + vect.z)

    def __sub__(self, vect):
        return self + -vect

    def __mul__(self, vect):
        if isinstance(vect, Vector):
            return self.x*vect.x + self.y*vect.y + self.z*vect.z
        return Vector(vect*self.x, vect*self.y, vect*self.z)

    def __rmul__(self, vect):
        return self * vect

    def abs2(self):
        return self * self

    def __abs__(self):
        return np.sqrt(self.abs2())

    def __xor__(self, vect):
        return Vector(self.y*vect.z - self.z*vect.y,
                      self.z*vect.x - self.x*vect.z,
                      self.x*vect.y - self.y*vect.x)

    def angle(self, vect):
        return np.arccos((self*vect) / (abs(self)*abs(vect)))


if __name__ == '__main__':
    a = Vector(1., 0., 0.)
    b = Vector(0., 1., 0.)
    c = Vector(0., 0., 0.)
    print a
    print b
    print a*b
    print 7*a
    print abs(a)
    print a^b
    print a + b
    print a + Vector(1., 0., 0.)
    print a == b
    print a == 0