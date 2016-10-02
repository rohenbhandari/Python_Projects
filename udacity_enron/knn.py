from sklearn.neighbors import NearestNeighbors, KNeighborsClassifier
import numpy as np
#from sklearn.metrics import 

X = np.array([[2., 1.], [-1., -1.], [-84., 84.]])
Y = np.array([0, 0, 1])
nbrs = KNeighborsClassifier(n_neighbors = 2, algorithm = 'kd_tree')
#distances, indices = nbrs.kneighbors(X)

nbrs.fit(X, Y)

print nbrs.predict([[-84, 84]])
