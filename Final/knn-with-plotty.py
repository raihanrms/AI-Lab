import plotly.graph_objects as go
import numpy as np
from sklearn.datasets import make_moons, make_s_curve
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

mesh_size = .02
margin = 0.5

# Load and split data

# Load the data from user input
# XR = int(input("Enter the number of rows for X:"))
# XC = int(input("Enter the number of columns for X:"))

# X = []
# print("Enter the values for X: ")
# for i in range(XR):
#     a = []
#     for j in range(XC):
#         a.append(int(input()))
#     X.append(a)


# YR = int(input("Enter the number of rows for y: "))
# YC = int(input("Enter the number of columns for y: "))

# y = []
# print("Enter the values for y: ")
# for i in range(YR):
#     b = []
#     for j in range(YC):
#         b.append(int(input()))
#     y.append(b)

X, y = make_moons(noise=0.3, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(
    X, y.astype(str), test_size=0.3, random_state=0)

# Create a mesh grid on which we will run our model
x_min, x_max = X[:, 0].min() - margin, X[:, 0].max() + margin
y_min, y_max = X[:, 1].min() - margin, X[:, 1].max() + margin
xrange = np.arange(x_min, x_max, mesh_size)
yrange = np.arange(y_min, y_max, mesh_size)
xx, yy = np.meshgrid(xrange, yrange)

# Create classifier, run predictions on grid
clf = KNeighborsClassifier(15, weights='uniform')
clf.fit(X, y)
Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
Z = Z.reshape(xx.shape)

trace_specs = [
    [X_train, y_train, '0', 'Train', 'square'],
    [X_train, y_train, '1', 'Train', 'circle'],
    [X_test, y_test, '0', 'Test', 'square-dot'],
    [X_test, y_test, '1', 'Test', 'circle-dot']
]

fig = go.Figure(data=[
    go.Scatter(
        x=X[y==label, 0], y=X[y==label, 1],
        name=f'{split} Split, Label {label}',
        mode='markers', marker_symbol=marker
    )
    for X, y, label, split, marker in trace_specs
])
fig.update_traces(
    marker_size=10, marker_line_width=1.5,
    marker_color="lightseagreen"
)

fig.add_trace(
    go.Contour(
        x=xrange,
        y=yrange,
        z=Z,
        showscale=False,
        colorscale='RdBu',
        opacity=0.5,
        name='Score',
        hoverinfo='all'
    )
)
fig.show()