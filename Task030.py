#Вычислить число c заданной точностью d.

import math
d = 0.001
d = str(d).split('.')
L = len(d[1])
M = str(math.pi)
print(float(M[:L+2]))