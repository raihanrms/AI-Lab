import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import itertools
from mlxtend.plotting import plot_decision_regions
import numpy as np

gs = gridspec.GridSpec(2, 2)

fig = plt.figure(figsize=(10,8))
clf1 = LogisticsRegression(random_state=1, solver='lbfgs')

labels = ['Logistic Regression']
for clf, lab, grd in zip([clf1],
                         labels,
                         itertools.product([0, 1], repeat=2)):

    clf.fit(X, y)
    ax = plt.subplot(gs[grd[0], grd[1]])
    fig = plot_decision_regions(X=X, y=y, clf=clf, legend=2)
    plt.title(lab)

plt.show()