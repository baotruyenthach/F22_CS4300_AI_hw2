from skspatial.objects import Plane, Points
from skspatial.plotting import plot_3d
import matplotlib.pyplot as plt
import numpy as np

def plot_plane(plane, pts):
    plot_3d(
        pts.plotter(c='k', s=50, depthshade=False),
        plane.plotter(alpha=0.2, lims_x=(-5, 5), lims_y=(0, 6)),
    )


def get_plane_from_weights(w):
    """
    ex: w = [4,2,3] -> plane equation: 4x + 2y - z + 3 = 0
    """    
    point = [0,0, w[2]]
    normal = [w[0], w[1], -1]
    return Plane(point=point, normal=normal)


data = np.array([[0, 0, 0], [3, 1, 5], [-5, 3, 3], [1, 4, 7], [-1, 5, 6]])

# TODO: Enter your weights here. Note: w.shape = (3,)
w = [0,0,0]

plane = get_plane_from_weights(w)
plot_plane(plane, Points(data))


plt.xlabel('x')
plt.ylabel('y')
plt.show()