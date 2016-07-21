import numpy as np


def isnumber(x):
    if type(x) in [float, np.float16, np.float32, np.float64, np.float, np.float, int, np.int, np.int32, np.int64,
                   np.uint32, np.uint64, np.int16, np.uint16, np.int8, np.uint8]:
        return True
    return False

FLOAT = np.float64


class Vector:
    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], np.ndarray):
                if len(args[0].shape) == 1:
                    if args[0].shape[0] > 1:
                        self.v = np.zeros(len(args[0]), FLOAT)
                        self.v[:] = args[0]
                    else:
                        raise ValueError("Cannot initiate 'Vector' with empty array.")
                else:
                    raise ValueError("The input array must be unidimensional.")
            elif isinstance(args[0], tuple) or isinstance(args[0], list):
                self.v = np.array(args[0]).astype(FLOAT)
            elif isnumber(args[0]):
                self.v = np.array([args[0]]).astype(FLOAT)
            else:
                raise TypeError("Single argument must be 'np.ndarray', 'list', 'tuple' or number not %s" % (type(args[0]),))
        elif len(args) > 1:
            self.v = np.zeros(len(args), FLOAT)
            for i in range(len(args)):
                if isnumber(args[i]):
                    self.v[i] = args[i]
                else:
                    raise TypeError("Arguments for 'Vector' must be numbers not %s." % (type(args[i]),))
        else:
            raise AttributeError("Cannot initiate 'Vector' with zero arguments.")
        self.dim = len(self.v)

    def __len__(self):
        return len(self.v)

    def __str__(self):
        s = '('
        for i in self.v:
            s += str(i) + ', '
        return s[:-2] + ')'

    def __repr__(self):
        return str(self)

    def dimMismatch(self, vect):
        raise ValueError("Dimensional mismatch for vectors with size %d & %d." % (len(self), len(vect)))

    def __getitem__(self, key):
        return self.v[key]

    def __eq__(self, vect):
        if isinstance(vect, Vector) and len(vect) == len(self):
            for i in range(len(self)):
                if self[i] != vect[i]:
                    return False
            return True
        if isnumber(vect) and vect == 0:
            return self == Vector([0]*len(self))
        return False

    def __ne__(self, vect):
        return not (self == vect)

    def __pos__(self):
        return Vector(self.v)

    def __neg__(self):
        return Vector(-self.v)

    def __add__(self, vect):
        if isinstance(vect, Vector):
            if len(self) == len(vect):
                return Vector(self.v + vect.v)
            self.dimMismatch(vect)
        raise TypeError("Addition isn't defined between 'Vector' and %s" % (type(vect),))

    def __sub__(self, vect):
        return self + -vect

    def __mul__(self, vect):
        if isinstance(vect, Vector):
            if len(self) == len(vect):
                return np.dot(self.v, vect.v)
            self.dimMismatch(vect)
        elif isnumber(vect):
            return Vector(vect*self.v)
        raise TypeError("Multiplication isn't defined between 'Vector' and %s" % (type(vect),))

    def __rmul__(self, vect):
        return self * vect

    def abs2(self):
        return self * self

    def __abs__(self):
        return np.sqrt(self.abs2())

    def __xor__(self, vect):
        if len(self) == len(vect):
            if len(self) == 3:
                return Vector(np.cross(self.v, vect.v))
            raise ValueError(
                "The cross product can only be calculated between 2 vector in 3 dimensions not %d." % (len(self),))
        self.dimMismatch(vect)

    def angle(self, vect):
        if not isinstance(vect, Vector):
            raise TypeError("Expected 'Vector' type got %s." % (type(Vector),))
        if not self.dim == vect.dim:
            self.dimMismatch(vect)
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