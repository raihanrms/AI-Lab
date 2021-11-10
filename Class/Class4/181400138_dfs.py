'''
Task: Basic dfs travering
CSE 432 S3
Name: Raihan Munim
ID: 181400138
Date: 10th Nov, 2021
'''

from collections import defaultdict

class Graph: # represents a directed graph
    def __init__(self): # with this we can create a default dictionary
        # default dic is a package to store a list of graph
        self.graphlist = defaultdict(list)
    
    # function to add edge to graph
    # this arguments we pass the value from main function, like one node to another
    def EdgeAddition(self, n, v):
        # we will pass the node(n) and v to a graph list
        self.graphlist[n].append(v)

    # dfs function
    # passing the nodes to the dfs
    def DFSFuction(self, v, visitNode):
        # marking the visited node and print it
        visitNode[v] = True
        print(v, end=' ')

    # recursion for all the vertices adjacent to vertex
        for i in self.graphlist[v]:
        # check the visit node, if not marked pass it to the dfs function again
                if visitNode[i] == False:
                    # recursion of this fuction
                    self.DFSFunction(i, visitNode) 

    # fuction to do dfs traversals
    def DFS(self, v):
        # mark all the vertices as not visited
        visitNode = [False] * (max(self.graphlist)+1)
        # call the recursive function
        self.DFSFuction(v, visitNode)

# main function object with class name
g = Graph()

# enter total number of edges
length = int(input("Enter total number of edges: "))
for i in range(length):
    # call value from user starting node and ending node
    x = int (input("First value: "))
    y = int (input("Second value: "))

    # call edge addition function to pass both variables
    g.EdgeAddition(x,y)

# get starting value from user
s = int(input("Enter a starting value: "))

# pass starting value to dfs function
g.DFS(s)

'''
Total number of edges = 7
Start node = 2
1st 2nd
0   1
0   2
1   2
2   0
2   3
3   1
3   2

starting value = 2
output 2 0 1 3

** Note: sometimes it gets runtime errors
'''