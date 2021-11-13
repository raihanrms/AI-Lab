'''
Task: DFS traversal from source to destination
CSE 432 S3
Name: Raihan Munim
ID: 181400138
Date: 12th Nov, 2021
'''
import matplotlib.pyplot as plt
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graphlist = defaultdict(list)
    
    
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printPath(self, u, destination, visited, path):
        visited[u] = True
        path.append(u)

        if u == destination:
            print 
            path
        
        else:
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printPath(i, destination, visited, path)
        
        path.pop()
        visited[u] = False

    def printAllPath(self, source, destination):
        visited = [False] * (self.V)
        path = []
        self.printPath(source, destination, visited, path)

g = Graph()

length = int(input("Enter number of edges: "))
for i in range(length):
    x = int(input("Edge: "))
    y = int(input("Vertice: "))
    g.addEdge(x,y)

source = int(input("Enter source: "))
destination = int(input("Enter destination: "))

print("All the different paths from %d to %d : " %(s, d))
g.printAllPath(source, destination)

g.draw(Graph, with_labels=True, font_weight='bold')
plt.show()

'''
Total edge = 8
Edges Vertices
0       1
0       2
0       3
2       0
2       1
2       3
1       3
1       4
4       0

Source = 2
Destination = 4
Path: *errors*
'''