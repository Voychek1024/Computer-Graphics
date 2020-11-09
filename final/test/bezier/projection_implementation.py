import math
import numpy as np

world_coords = np.array([[-1.0, -1.0, 0.9602649717277704, 1], [-1.0, 1.0, 0.20990424846665412, 1],
                         [1.0, -1.0, 0.15695828735128203, 1], [1.0, 1.0, 0.906161006959773, 1]])

view = [[4, 3, 3, 1], [0, 0, 0, 1], [0, 0, 1, 1]]

perspective = np.array([45.0, 800.0 / 800.0, 0.1, 100.0])

projection_mat = np.array([[2.4142137, 0., 0., 0.],
                           [0., 2.4142137, 0., 0.],
                           [0., 0., -1.002002, -1.],
                           [0., 0., -0.2002002, 0.]])
model_mat = np.array([[-0.70710677, - 0.4082483, 0.5773503, 0.],
                      [0.70710677, -0.4082483, 0.5773503, 0.],
                      [0., 0.8164966, 0.5773503, 0.],
                      [0., 0., -5.1961527, 1.]])
view_port = np.array([0, 0, 800, 800])
mouse_x, mouse_y = 400, 248

"""
for item in world_coords:
    print("item", item)
    result = item @ (model_mat @ projection_mat).T * view_port
    print("proj", result)
"""



