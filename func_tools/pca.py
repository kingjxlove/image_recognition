import numpy as np
from sklearn.decomposition import PCA

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
# 降维
pca = PCA(n_components=1)
newX = pca.fit_transform(X)  # 等价于pca.fit(X) pca.transform(X)
# 数据还原
invX = pca.inverse_transform(newX)

print(X, X.shape)
print(pca)
print(newX, newX.shape)
print(invX, invX.shape)
