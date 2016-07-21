import numpy as np

FLOAT = np.float64


class Vectors:
    def __init__(self, vec):
        if not isinstance(vec, np.ndarray):
            if not (type(vec) == list or type(vec) == tuple):
                raise TypeError("Argument must be 'ndarray', list or tuple not %s" % (type(vec),))
            self.vec = np.array(vec)

        if vec.shape[-1] != 3:
            raise ValueError("Last dimension of array must be 3 not %d." % (vec.shape[-1],))

        self.vec = vec.astype(FLOAT)
        self.shape = vec.shape[:-1]

    def __str__(self):
        return str(self.vec)

    def __repr__(self):
        return str(self)

    def __neg__(self):
        return Vectors(-self.vec)

    def __pos__(self):
        return Vectors(+self.vec)

    def __add__(self, vect):
        return Vectors(self.vec + vect.vec)

    def __sub__(self, vect):
        return Vectors(self.vec - vect.vec)

    def __mul__(self, vect):
        if isinstance(vect, Vectors):
            a = np.swapaxes(self.vec, -1, 0)
            b = np.swapaxes(vect.vec, -1, 0)
            return np.swapaxes(a[0]*b[0] + a[1]*b[1] + a[2]*b[2], -1, 0)
        if isinstance(vect, np.ndarray):
            if self.vec.shape[:-1] != vect.shape:
                raise ValueError("Dimensional mismatch for shapes %s & %s" % (str(self.vec.shape[:-1]), str(vect.shape)))
            a = np.swapaxes(self.vec, -1, 0)
            return a[0]*vect + a[1]*vect + a[2]*vect
        return Vectors(self.vec * vect)

    def __rmul__(self, vect):
        return self * vect

    def __xor__(self, vect):
        return Vectors(np.cross(self.vec, vect.vec))

    def abs2(self):
        return self * self

    def __abs__(self):
        return np.sqrt(self.abs2())


if __name__ == '__main__':
    a = Vectors( np.array([[1., 2., 3.], [4., 5., 6.]]) )
    b = Vectors( np.array([[1., 1., 0.], [0., 0., 1.]]) )
    #print a*b
    print a, '\n\n'
    print a*b
