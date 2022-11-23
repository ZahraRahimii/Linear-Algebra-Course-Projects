import matplotlib.pyplot as plt
import numpy as np

k = 500
path = "img1.bmp"
img = plt.imread(path)

r = img[:, :, 0]
g = img[:, :, 1]
b = img[:, :, 2]

ur, sr, vhr = np.linalg.svd(r)
ur2 = ur[:, 0:k]
sr2 = np.zeros((k, k), dtype=float)
vhr2 = vhr[0:k, :]

ug, sg, vhg = np.linalg.svd(g)
ug2 = ug[:, 0:k]
sg2 = np.zeros((k, k), dtype=float)
vhg2 = vhg[0:k, :]

ub, sb, vhb = np.linalg.svd(b)
ub2 = ub[:, 0:k]
sb2 = np.zeros((k, k), dtype=float)
vhb2 = vhb[0:k, :]

for i in range(k):
    sr2[i][i] = sr[i]; sg2[i][i] = sg[i]; sb2[i][i] = sb[i]

rr = np.dot(ur2, np.dot(sr2, vhr2))
gg = np.dot(ug2, np.dot(sg2, vhg2))
bb = np.dot(ub2, np.dot(sb2, vhb2))

plt.imshow(np.dstack((rr, gg, bb)).astype(np.uint8))
plt.show()