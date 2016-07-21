from Vector import Vector

class Ray:
    def __init__(self, start, direction):
        if not isinstance(start, Vector):
            raise TypeError("The 'start' argument must be of class 'Vector' not %s." % (type(start),))
        if not isinstance(direction, Vector):
            raise TypeError("The 'direction' argument must be of class 'Vector' not %s." % (type(direction),))
        if direction == 0:
            raise ValueError("The 'direction' cannot be a zero vector.")
        if start.dim != direction.dim:
            raise ValueError("Dimensional mismatch for 'start' in %d dimensions and 'direction' in %d dimensions." % (start.dim, direction.dim))
        self.start = start
        self.direction = direction
        self.dim = start.dim

    def __str__(self):
        return 'ray: %s + d*%s, d > 0' % (str(self.start), str(self.direction))

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    s = Vector(0, 0., 0)
    d = Vector((1, 0, 0))
    r = Ray(s, d)
    print r