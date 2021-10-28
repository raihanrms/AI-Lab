## Breadth first search on a directed matrix, getting the shortest path
# Incomplete implementation, tried what I understood
# Raihan Munim <181400138>

# inbuilt queue data structure
# using double ended queue, but using it as a queue
from collections import deque
from collections import defaultdict 

# using this function to create a adjagency matrix in order to
# implement a weighted matrix I can make the bfs to traverse on
def printmatrix(matrix):
    # row and column with len matrix
    r,c = len(matrix),len(matrix[0])
    for i in range(r):
        for j in range(c):
            print(matrix[i][j],end=" ")
        print()
# v = vertices, e = edges, w = weight        
v,e = map(int,input().split())
# would generate a matrix for v(sqr)
matrix = [[0]*v for i in range(v)]
# utilizing the matrix
for i in range(e):
    u,v,w = map(str,input().split())
    # converting ascii values to matrix indices
    u = ord(u) - ord('A')
    v = ord(v) - ord('A')
    w = int(w)
    matrix[u][v] = w # Weight / Cost in case of edge
printmatrix(matrix)

# tried to do bfs on the weighted adj matrix
def AIBFS(matrix, start, visited, path):
    # initializing the start nodes
    queue = deque() # has the ability to dequeue and enque from both ends
    path.append(start)
    queue.append(start)

    visited[start] = True
    while len(queue) != 0:
        tempNode = queue.popleft()
        for neighbour in matrix[tempNode]:
            if visited[neighbour] == False:
                path.append(neighbour)
                queue.append(neighbour)
                visited[neighbour] = True
    return path

matrix = defaultdict(matrix)
v,e = map(int,input().split())
for i in range(e):
    u,v = map(str,input().split())
    matrix[u].append(v)
    matrix[v].append(u)

start = print(str,"Source node: ", input)
path = []
visited = defaultdict(bool)
traversedPath = AIBFS(matrix, start, visited, path)
print(traversedPath)

'''
test case:
5 6
A B 5
A C 6
B D 15
C E 4
D F 12
E D 5
'''