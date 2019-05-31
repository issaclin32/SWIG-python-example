import numpy as np
import find_nearest
import random

x = np.array([random.randint(0,600) for _ in range(10)])
y = np.array([random.randint(0,600) for _ in range(10)])
wx = np.array([random.randint(0,600) for _ in range(10)])
wy = np.array([random.randint(0,600) for _ in range(10)])
sx = np.array([random.randint(0,600) for _ in range(10)])
sy = np.array([random.randint(0,600) for _ in range(10)])

res = find_nearest.find(x, y, wx, wy, sx, sy, True)
print(res)