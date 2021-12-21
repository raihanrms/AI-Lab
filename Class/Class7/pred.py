import numpy as np
from sklearn import neighbors, datasets
from sklearn import preprocessing

n_neighbors = 6

# import some data to play with
iris = datasets.load_iris()

# prepare data
X = iris.data[:, :2]
y = iris.target
h = .02

# we create an instance of Neighbours Classifier and fit the data.
clf = neighbors.KNeighborsClassifier(n_neighbors, weights='distance')
clf.fit(X, y)

# make prediction
sl = raw_input('Enter sepal length (cm): ')
sw = raw_input('Enter sepal width (cm): ')
dataClass = clf.predict([[sl,sw]])
print('Prediction: '),

if dataClass == 0:
print('Iris Setosa')
elif dataClass == 1:
print('Iris Versicolour')
else:
print('Iris Virginica')