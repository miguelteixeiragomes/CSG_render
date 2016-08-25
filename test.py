from Sphere import Sphere
from Ray import Ray
from Rays import Rays
from Vector import Vector
from Vectors import Vectors
import pylab as pl
import numpy as np
import time

s = Sphere(Vector(0, 0, 0), 1)
eye = Vector(0, 0, -5)
screen = np.meshgrid(np.linspace(-2, 2, 5), np.linspace(-2, 2, 5))
rays1 = np.zeros(screen[0].shape, type(Ray(Vector(0, 0, 0), Vector(1, 0, 0))))
origins = np.zeros(list(screen[0].shape) + [3])
directions = np.zeros(list(screen[0].shape) + [3])
for i in range(rays1.shape[0]):
    for j in range(rays1.shape[1]):
        origins[i, j, 0] = eye[0]
        origins[i, j, 1] = eye[1]
        origins[i, j, 2] = eye[2]
        directions[i, j, 0] = (Vector(screen[0][i, j], screen[1][i, j], 1) - eye)[0]
        directions[i, j, 1] = (Vector(screen[0][i, j], screen[1][i, j], 1) - eye)[1]
        directions[i, j, 2] = (Vector(screen[0][i, j], screen[1][i, j], 1) - eye)[2]
        rays1[i, j] = Ray(eye, Vector(screen[0][i, j], screen[1][i, j], 1) - eye)
rays2 = Rays(Vectors(origins), Vectors(directions))

img1 = np.zeros(rays1.shape)
T = time.clock()
for i in range(rays1.shape[0]):
    for j in range(rays1.shape[1]):
        intr = s.intersectionWithRay(rays1[i, j])[2]
        img1[i, j] = np.nan if intr is None else .5 * np.pi - intr
print "single:  ", time.clock() - T


T = time.clock()
print "START"
img2 = s.intersectionWithRays(rays2)[0]
print "multiple:", time.clock() - T


pl.subplot(121)
pl.imshow(img1, cmap ='Greys_r')
pl.axis('off')
pl.subplot(122)
pl.imshow(img2, cmap ='Greys_r')
pl.axis('off')
pl.show()