class Vertex:
    def __init__(self, key):
        # unique ID for vertex         
        self.id = key
        # dict of connected nodes        
        self.connected_to = {}
    
    def add_neighbor(self, neighbor, weight=0):
        # Add an entry to the connected_to dict with a given weight
        self.connected_to[neighbor] = weight
        
    def __str__(self):
        # override __str__ for printing         
        return(str(self.id) + ' connected to: ' + str([x.id for x in self.connected_to]))
    
    def get_connections(self):
        # return keys from connected_to dict         
        return self.connected_to.keys()
    def get_id(self):
        # return vertex id's         
        return self.id
    
    def get_weight(self):
        # return weights of edges connected to vertex
        return self.connected_to[neighbor]

class Graph:
    def __init__(self):
        # dictionary of vertices         
        self.vertices_list = {}
        # vertex count         
        self.num_vertices = 0
        
    def add_vertex(self, key):
        # increment counter when adding vertex         
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(key)
        self.vertices_list[key] = new_vertex
        return new_vertex
    
    def get_vertex(self, n):
        # check if vertex exists, return if True         
        if n in self.vertices_list:
            return self.vertices_list[n]
        else:
            return None
        
    def __contains__(self, n):
        # override __contains__ to list all vertices in Graph object         
        return n in self.vertices_list
    
    def add_edge(self, s, f, cost=0):
        # add edge to graph; s = start node; e = end node         
        if s not in self.vertices_list:
            nv = self.add_vertex(s)
        if f not in self.vertices_list:
            nv = self.add_vertex(f)
        self.vertices_list[s].add_neighbor(self.vertices_list[f], cost)
        
    def get_vertices(self):
        # return keys of vertices in Graph         
        return self.vertices_list.keys()
    
    def __iter__(self):
        # override __iter__ to return iterable of vertices        
        return iter(self.vertices_list.values())
    
node_names = ["A", "B", "C",
              "D", "E", "F",
              "G"]
# Instantiate graph object and add vertices 
g = Graph()
for i in node_names:
    g.add_vertex(i)
# add a bunch of edges between vertices 
g.add_edge('A','B')
g.add_edge('B','C')
g.add_edge('C','E')
g.add_edge('E','D')
g.add_edge('D','B')
g.add_edge('E','F')
g.add_edge('B','E')
for v in g:
    for w in v.get_connections():
        print("(%s, %s)" % (v.get_id(), w.get_id()))

# list our vertices 
for i in node_names:
    print(g.get_vertex(i))

from collections import deque

def breadth_first_search(starting_node, goal_node):
    visited_nodes = set()
    queue = deque([starting_node])
    
    while len(queue) > 0:
        node = queue.pop()
        if node in visited_nodes:
            continue
        
        visited_nodes.add(node)
        if node.get_id == goal_node.get_id:
            return True
        
        for n in node.connected_to:
            if n not in visited_nodes:
                queue.appendleft(n)
    return False

breadth_first_search(g.get_vertex('A'), g.get_vertex('G'))

import networkx as nx

import matplotlib.pyplot as plt

edges = [('A','B'),('B','C'),('C','E'),
         ('E','D'),('D','B'),('E','F'),
         ('B','E')]

networkx_graph = nx.Graph()

for node in node_names:
    networkx_graph.add_node(node)

networkx_graph.add_edges_from(edges)

nx.draw_networkx(networkx_graph)

networkx_graph_1 = nx.dense_gnm_random_graph(10,10)

nx.draw_networkx(networkx_graph_1)

# quick hack to traverse the iterables returned 
for node in nx.nodes(networkx_graph_1):
    neighbors = []
    for neighbor in nx.all_neighbors(networkx_graph_1, node):
        neighbors.append(neighbor)
    print("Node %s has neighbors : %s" % (node, neighbors))   

[[neighbor for neighbor in nx.all_neighbors(networkx_graph_1, node)] for node in nx.nodes(networkx_graph_1)]
print(list(nx.bfs_edges(networkx_graph_1, 0)))
print(list(nx.dfs_edges(networkx_graph_1, 0)))