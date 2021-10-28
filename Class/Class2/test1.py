from collections import defaultdict

# class represents a directed graph using 
# adjacency list representation
class Graph:

	def __init__(self,vert):
		self.V = vert #No. of vertices
		self.V_org = vert
		self.graph = defaultdict(list) # default dictionary to store graph

	# function to add an edge to graph
	def addEdge(self,u,v,w):
		if w == 1:
			self.graph[u].append(v)
		else:	
			# split all edges of weight 2 into two 
            # edges of weight 1 each. 
			self.graph[u].append(self.V)
			self.graph[self.V].append(v)
			self.V = self.V + 1
	
	# To print the shortest path stored in parent[]
	def printPath(self, parent, j):
		pathLength = 1
		if parent[j] == -1 and j < self.V_org : #Base Case : If j is source
			print(j),
			return 0 # when parent[-1] then path length = 0	
		l = self.printPath(parent , parent[j])
		pathLength = l + pathLength

		# print node only if its less than original node length.
		if j < self.V_org :
			print(j),

		return pathLength

	# this fuction will assume that weight of every edge is 1
	def findShortestPath(self,src, dest):

		# Mark all the vertices as not visited 
		visited =[False]*(self.V)
		parent =[-1]*(self.V)

		# Create a queue for BFS
		queue=[]

		# Mark the source node as visited and enqueue it
		queue.append(src)
		visited[src] = True

		while queue :
			# Dequeue a vertex from queue
			s = queue.pop(0)
			
			# if s = dest then print the path and return
			if s == dest:
				return self.printPath(parent, s)
			
			# Getting all adjacent vertices of the dequeued vertex s
			# If a adjacent has not been visited, then mark it
			# visited and enqueue it
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True
					parent[i] = s

# Create a graph given in the above diagram
g = Graph(5)
g.addEdge(0, 1, 2)
g.addEdge(0, 2, 2)
g.addEdge(1, 2, 1)
g.addEdge(1, 4, 1)
g.addEdge(2, 0, 1)
g.addEdge(2, 4, 2)
g.addEdge(4, 4, 2)


src = 0; 
dest = 4;
print ("Shortest Path between %d and %d is " %(src, dest)),
l = g.findShortestPath(src, dest)
print ("\nShortest Distance between %d and %d is %d " %(src, dest, l)),

