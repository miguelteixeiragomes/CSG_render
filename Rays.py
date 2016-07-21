from Vectors import Vectors, np


class Rays:
    def __init__(self, origins, directions):
        if not isinstance(origins, Vectors):
            raise TypeError("Expected 'origins' to be of class 'Vectors' not %s" % (type(origins),))
        if not isinstance(origins, Vectors):
            raise TypeError("Expected 'directions' to be of class 'Vectors' not %s" % (type(directions),))
        if origins.shape == directions.shape:
            raise ValueError("" % (origins.shape, directions.shape))
        directions = np.swapaxes(directions, -1, 0)
        if np.sum((1*(directions[0] == 0)) * (1*(directions[1] == 0)) * (1*(directions[2] == 0))) > 0:
            raise ValueError("All vectors in 'directions' must be nonzero.")
        directions = np.swapaxes(directions, -1, 0)

        self.origins = origins
        self.directions = directions
        self.shape = origins.shape[:]

    def __str__(self):
        return "Rays: %s[n] + d*%s[n], d > 0, n as all indices" % (str(self.origins), str(self.directions))

    def __repr__(self):
        return str(self)