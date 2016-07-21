from Rays import Rays
from Vectors import Vectors, np


class Sphere:
    def __init__(self, centers, radii):
        if not isinstance(centers, Vectors):
            raise TypeError("The 'centers' argument must be of class 'Vectors' not %s." % (type(center),))
        if centers.shape != radii.shape:
            raise ValueError("Dimensional mismatch for shapes %d & %d" % (centers.shape, radii.shape))
        if np.sum(1*(radii <= 0)) > 0:
            raise ValueError("All 'radii' must be greater than 0.")
        self.centers = centers
        self.radii = radii
        self.shape = centers.shape[:]

    def __str__(self):
        return 'sphere: |r - %s[n]| < %s[n], n as all indices' % (str(self.center), str(self.radius))

    def __repr__(self):
        return str(self)

    def intersectionWithRays(self, rays):
        if not isinstance(rays, Rays):
            raise TypeError("Intersections must be with objects of type 'Rays' not %s" % (type(rays),))

        o_c = rays.origins - self.center
        lo_c = rays.direction * o_c
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