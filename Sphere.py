import numpy as np
from Vector import Vector
from Vectors import Vectors
from Ray import Ray
from Rays import Rays


class Sphere:
    def __init__(self, center, radius):
        if not isinstance(center, Vector):
            raise TypeError("The 'center' argument must be of class 'Vectors' not %s." % (type(center),))
        if radius <= 0:
            raise ValueError("The 'radius' must be greater than 0.")
        self.center = center
        self.radius = radius

    def __str__(self):
        return 'sphere: |r - %s| < %s' % (self.center, self.radius)

    def __repr__(self):
        return str(self)

    def intersectionWithRay(self, ray):
        if not isinstance(ray, Ray):
            raise TypeError("Intersections must be with objects of type 'Rays' not %s" % (type(ray),))

        o_c = ray.origin - self.center
        lo_c = ray.direction * o_c
        abs2l = ray.direction.abs2()
        b2_4ac = lo_c*lo_c - abs2l*(o_c.abs2() - self.radius*self.radius)
        if b2_4ac <= 0: # Still deciding weather single point intersection count as intersections
            return None, None, None
        # if b2_4ac == 0:
        #     return -lo_c / abs2l, .5*np.pi
        b2_4ac = np.sqrt(b2_4ac)
        d1 = (-lo_c - b2_4ac)/abs2l
        d2 = (-lo_c + b2_4ac)/abs2l
        d = d1 if d1 > 0 else d2
        intr = ray.origin + d*ray.direction
        return d, intr, (-ray.direction).angle(intr - self.center)

    def intersectionWithRays(self, rays):
        if not isinstance(rays, Rays):
            raise TypeError("Intersections must be with objects of type 'Rays' not %s" % (type(rays),))

        o_c = rays.origins - self.center
        lo_c = rays.directions * o_c
        abs2l = rays.directions.abs2()
        b2_4ac = lo_c*lo_c - abs2l*(o_c.abs2() - self.radius*self.radius)
        b2_4ac[np.where(b2_4ac <= 0)] = np.nan
        indices = np.where(b2_4ac > 0)
        b2_4ac[indices] = np.sqrt(b2_4ac[indices])
        #print b2_4ac
        d = (-lo_c - b2_4ac)/abs2l
        print d
        d[np.where(d <= 0)] = np.nan
        print isinstance(d*rays.directions, np.ndarray)
        intr = rays.origins + d*rays.directions
        return d, intr, (-rays.directions).angle(intr - self.center)


if __name__ == '__main__':
    c = Vector(0, 0, 0)
    s = Sphere(c, 1)
    print s
    r = Ray(Vector(-2, .5, 0), Vector(1, 0, 0))
    print s.intersectionWithRay(r)
