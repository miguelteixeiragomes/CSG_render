from Vector_Vectors import np, FLOAT, Vector, Vectors


class Vector(Vector):
    def __init__(self, *args):
        if len(args) == 3:
            self.x = FLOAT(float(args[0]))
            self.y = FLOAT(float(args[1]))
            self.z = FLOAT(float(args[2]))
        elif len(args) == 1:
            try:
                self.x = FLOAT(float(args[0][0]))
                self.y = FLOAT(float(args[0][1]))
                self.z = FLOAT(float(args[0][2]))
            except:
                raise TypeError("The single argument must have '__getitem__' method.")
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
            return vect == self
        if isinstance(vect, Vector):
            return self.x == vect.x and self.y == vect.y and self.z == vect.z
        if vect == 0:
            return self.x == 0 and self.y == 0 and self.z == 0
        raise TypeError("Expected 'Vector', 'Vectors' or an equivalent to 0 not %s." % (type(vect),))

    def __ne__(self, vect):
        ret = self == vect
        if type(ret) == bool:
            return not ret
        return ~ret

    def __pos__(self):
        return Vector(self.x, self.y, self.z)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __radd__(self, vect):
        return Vector(self.x + vect.x, self.y + vect.y, self.z + vect.z)

    def __sub__(self, vect):
        return self + -vect

    def __mul__(self, vect):
        #print 'mul vector 1'
        if isinstance(vect, Vector):
            #print 'mul vector 2'
            return self.x*vect.x + self.y*vect.y + self.z*vect.z
        if isinstance(vect, Vectors):
            #print 'mul vector 3'
            return vect * self
        return Vector(vect*self.x, vect*self.y, vect*self.z)

    def __rmul__(self, vect):
        #print 'rmul vector'
        return self * vect

    def abs2(self):
        return self * self

    def __abs__(self):
        return np.sqrt(self.abs2())

    def __pow__(self, vect):
        return Vector(self.y*vect.z - self.z*vect.y,
                      self.z*vect.x - self.x*vect.z,
                      self.x*vect.y - self.y*vect.x)

    def angle(self, vect):
        if isinstance(vect, Vector):
            return np.arccos((self*vect) / (abs(self)*abs(vect)))
        if isinstance(vect, Vectors):
            return vect.angles(self)
        raise TypeError("Expected 'Vector' or 'Vectors' not %s." % (str(vect),))

    def __xor__(self, vect):
        return self.angle(vect)
