from Vector import Vector

class Ray:
    def __init__(self, origin, direction):
        if not isinstance(origin, Vector):
            raise TypeError("The 'origin' argument must be of class 'Vector' not %s." % (type(origin),))
        if not isinstance(direction, Vector):
            raise TypeError("The 'direction' argument must be of class 'Vector' not %s." % (type(direction),))
        if direction == 0:
            raise ValueError("The 'direction' cannot be a zero vector.")
        self.origin = origin
        self.direction = direction

    def __str__(self):
        return 'ray: %s + d*%s, d > 0' % (str(self.origin), str(self.direction))

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    s = Vector(0, 0., 0)
    d = Vector((1, 0, 0))
    r = Ray(s, d)
    print r