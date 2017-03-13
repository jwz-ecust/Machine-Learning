from matplotlib.collections import LineCollection
import numpy as np
import matplotlib.pyplot as plt
from sklearn.isotonic import IsotonicRegression
np.random.seed(1)
x1 = np.arange(50)
y1 = x1 + 50 * np.random.rand(50)

x2 = np.arange(50)
ir = IsotonicRegression()
y2 = ir.fit_transform(x1, y1)


segments = [[[x1[i], y1[i]], [x2[i], y2[i]]] for i in range(50)]
lc = LineCollection(segments, zorder=0)

lc.set_array(np.ones(len(y1)))

lc.set_linewidth(0.5 * np.ones(50))

fig = plt.figure()
plt.plot(x1, y1, 'r.', markersize=20)
plt.plot(x2, y2, 'g.-', markersize=20)
plt.gca().add_collection(lc)
plt.legend(("1", "2"), loc="lower right")
plt.show()
