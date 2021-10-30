# CSE 432 
# Artificial intelligence lab
# Raihan Munim <181400138>

## Breadth first search on a directed matrix, getting the shortest path

from collections import defaultdict
# directed graph using adjacency list representation
class Graph:
    def __init__(self):
        # default dictonary to store graph 
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        # function to add an edge to graph
        self.graph[u].append(v)
    
    # function to print bfs of graph
    def BFS(self,s):
        # mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
        
        # create a queue for bfs
        queue = []

        # mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            
            # dequeue a vertex from queue and print it 
            s = queue.pop(0)
            print (s,end=" ")

            # Get all adjacent vertices of the dequeued vertex s. 
            # If a adjacent has not been visited, 
            # then mark it visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                  visited[i] = True

# create the graph 
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,1)
g.addEdge(3,2)
g.addEdge(4,3)
g.addEdge(4,4)

print("Following is BFS Traversal")
source = int(input("Enter Source node: "))
print("Shortest path: ")
g.BFS(source)