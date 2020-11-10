from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np

ambient_strength = 0.1

light_color = np.array([1.0, 1.0, 1.0])
toy_color = np.array([0.0, 0.5, 0.5])

ambient = ambient_strength * light_color

print(ambient * toy_color)
