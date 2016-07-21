from Sphere import Sphere
from Ray import Ray
from Vector import Vector, np
import pylab as pl

s = Sphere(Vector(0, 0, 0), 1)
eye = Vector(0, 0, -2)
screen = np.meshgrid(np.linspace(-2, 2, 201), np.linspace(-2, 2, 201))
rays = np.zeros(screen[0].shape, type(Ray(Vector(0, 0, 0), Vector(1, 0, 0))))
for i in range(rays.shape[0]):
    print '%d/%d' % (i, rays.shape[0])
    for j in range(rays.shape[1]):
        rays[i, j] = Ray(eye, Vector(screen[0][i, j], screen[1][i, j], 1) - eye)

img = np.zeros(rays.shape)
for i in range(rays.shape[0]):
    print '%d/%d' % (i, rays.shape[0])
    for j in range(rays.shape[1]):
        intr = s.intersectionWithRay(rays[i, j])[1]
        img[i, j] = 0. if intr is None else .5*np.pi - intr

pl.imshow(img, cmap = 'Greys_r')
pl.show()