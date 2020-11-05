import math
import numpy as np

model = [[-1.0, -1.0, 0.3417820828566388, 1], [-1.0, 1.0, 0.9809028662880951, 1],
         [1.0, -1.0, 0.6534702718528095, 1], [1.0, 1.0, 0.9887919354139622, 1]]

view = [[4, 3, 3], [0, 0, 0], [0, 0, 1]]

projection_matrix = np.array([[2.4142137, 0, 0, 0],
                     [0, 2.4142137, 0, 0],
                     [0, 0, -1.002002, -1],
                     [0, 0, -0.2002002, 0]])
model_matrix = np.array([[-0.70710677, -0.4082483, 0.5773503, 0.],
                [0.70710677, -0.4082483, 0.5773503, 0.],
                [0., 0.8164966, 0.5773503, 0.],
                [0., 0., -5.1961527, 1.]])

for item in model:
    print("item", item)
    result = projection_matrix @ model_matrix @ item
    print("proj", result)
    result = result / result[3]
    print(result)
