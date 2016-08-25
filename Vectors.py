from Vector_Vectors import np, FLOAT, Vector, Vectors
import time


class Vectors(Vectors):
    def __init__(self, vec):
        if vec is None:
            self.vec = None
            self.shape = None
        else:
            if not isinstance(vec, np.ndarray):
                if not (type(vec) == list or type(vec) == tuple):
                    raise TypeError("Argument must be 'numpy.ndarray', list or tuple not %s" % (type(vec),))
                self.vec = np.array(vec)
            else:
                self.vec = vec

            if self.vec.shape[-1] != 3:
                raise ValueError("Last dimension of array must be 3 not %d." % (self.vec.shape[-1],))

            self.vec = self.vec.astype(FLOAT)
            self.shape = self.vec.shape[:-1]
            for i in range(-1, -len(self.vec.shape), -1):
                self.vec = np.swapaxes(self.vec, i, i - 1)

    def __str__(self):
        return str(self.vec)

    def __repr__(self):
        return str(self)

    def __eq__(self, vect):
        if isinstance(vect, Vectors):
            return (self.vec[0] == vect.vec[0]) & (self.vec[1] == vect.vec[1]) & (self.vec[2] == vect.vec[2])
        if isinstance(vect, Vector):
            return (self.vec[0] == vect[0]) & (self.vec[1] == vect[1]) & (self.vec[2] == vect[2])
        if vect == 0:
            return (self.vec[0] == 0) & (self.vec[1] == 0) & (self.vec[2] == 0)
        raise TypeError("Expected 'Vector', 'Vectors' or an equivalent to 0 not %s." % (type(vect),))

    def __ne__(self, vect):
        ret = self == vect
        if type(ret) == bool:
            return not ret
        return ~ret

    def __neg__(self):
        return Vectors(-self.vec)

    def __pos__(self):
        return Vectors(+self.vec)

    def __add__(self, vect):
        if isinstance(vect, Vectors):
            new = Vectors(None)
            new.vec = np.zeros(self.vec.shape, FLOAT)
            new.vec = self.vec + vect.vec
            new.shape = new.vec.shape[1:]
            return new
        if isinstance(vect, Vector):
            new = Vectors(None)
            new.vec = np.zeros(self.vec.shape, FLOAT)
            new.vec[:] = self.vec[:]
            new.vec[0] += vect[0]
            new.vec[1] += vect[1]
            new.vec[2] += vect[2]
            new.shape = new.vec.shape[1:]
            return new
        raise TypeError("__add__ operation undefined between 'Vectors' & %s." % (type(vect),))

    def __radd__(self, vect):
        return self + vect

    def __sub__(self, vect):
        return self + -vect

    def __rsub__(self, vect):
        return -self + vect

    def __mul__(self, vect):
        print 'mul vectors 1'
        if isinstance(vect, Vectors):
            print 'mul vectors 2'
            return self.vec[0]*vect.vec[0] + self.vec[1]*vect.vec[1] + self.vec[2]*vect.vec[2]
        if isinstance(vect, np.ndarray):
            print 'mul vectors 3'
            if self.shape == vect.shape:
                print 'mul vectors 4'
                new = Vectors(None)
                new.vec = np.zeros(self.vec.shape, FLOAT)
                new.vec[:] = self.vec[:]
                new.vec[0] *= vect
                new.vec[1] *= vect
                new.vec[2] *= vect
                new.shape = self.shape
                return new
            raise ValueError("Dimensional mismatch for shapes %s & %s" % (str(self.shape), str(vect.shape)))
        if isinstance(vect, Vector):
            print 'mul vectors 5'
            return self.vec[0]*vect[0] + self.vec[1]*vect[1] + self.vec[2]*vect[2]
        print 'yo1'
        new = Vectors(None)
        print 'yo2'
        new.vec = np.zeros(self.vec.shape, FLOAT)
        print 'yo3'
        new.vec[:] = self.vec[:]
        print 'yo4'
        new.vec *= vect
        print 'yo5'
        new.shape = self.shape
        print 'yo6'
        return new

    def __rmul__(self, vect):
        print 'rmul vectors'
        print "\t%s" % type(vect)
        return self * vect

    def __pow__(self, vect):
        return Vectors(np.cross(self.vec, vect.vec))

    def abs2(self):
        return self * self

    def __abs__(self):
        return np.sqrt(self.abs2())

    def angles(self, vect):
        if isinstance(vect, Vectors):
            return np.arccos((self * vect) / np.sqrt(self.abs2() * vect.abs2()))
        if isinstance(vect, Vector):
            return np.arccos((self * vect) / np.sqrt(self.abs2() * vect.abs2()))
        raise TypeError("Expected 'Vector' or 'Vectors' not %s." % (str(vect),))

    def __xor__(self, vect):
        return self.angles(vect)
