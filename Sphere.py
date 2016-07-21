from Ray import Ray
from Vector import Vector, isnumber, np


class Sphere:
    def __init__(self, center, radius):
        if not isinstance(center, Vector):
            raise TypeError("The 'center' argument must be of class 'Vector' not %s." % (type(center),))
        if not isnumber(radius):
            raise TypeError("The 'center' argument must be of a number not %s." % (type(radius),))
        if radius == 0:
            raise ValueError("The 'radius' of the sphere cannot be 0.")
        self.center = center
        self.radius = radius
        self.dim = center.dim

    def __str__(self):
        return 'sphere: |r - %s| < %s' % (str(self.center), str(self.radius))

    def __repr__(self):
        return str(self)

    def intersectionWithRay(self, ray):
        if not isinstance(ray, Ray):
            raise TypeError("Intersections must be with objects of type 'Ray' not %s" % (type(ray),))
        if self.dim != ray.dim:
            ValueError("Dimensional mismatch for 'Sphere' in %d dimensions and 'Ray' in %d dimensions." % (
            self.dim, ray.dim))

        o_c = ray.start - self.center
        lo_c = ray.direction * o_c
        abs2l = ray.direction.abs2()
        b2_4ac = lo_c*lo_c - abs2l*(o_c.abs2() - self.radius*self.radius)
        if b2_4ac < 0:
            return None, None
        if b2_4ac == 0:
            return -lo_c / abs2l, .5*np.pi
        b2_4ac = np.sqrt(b2_4ac)
        d1 = (-lo_c - b2_4ac)/abs2l
        d2 = (-lo_c + b2_4ac)/abs2l
        d = d1 if d1 > 0 else d2
        intr = ray.start + d*ray.direction
        return intr, (-ray.direction).angle(intr - self.center)


if __name__ == '__main__':
    s = Sphere(Vector(0, 0, 0), 1)
    r = Ray(Vector(-2, .5, 0), Vector(1, 0, 0))
    print s.intersectionWithRay(r)