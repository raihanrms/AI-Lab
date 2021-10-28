## Breadth first search, getting the shortest path
# Incomplete implementation, tried what I understood
# Raihan Munim <181400138>

# inbuilt queue data structure
# using double ended queue, but using it as a queue
from collections import deque
from collections import defaultdict 

def printmatrix(matrix):
    r,c = len(matrix),len(matrix[0])
    for i in range(r):
        for j in range(c):
            print(matrix[i][j],end=" ")
        print()
        
v,e = map(int,input().split())
matrix = [[0]*v for i in range(v)]
for i in range(e):
    u,v,w = map(str,input().split())
    u = ord(u) - ord('A')
    v = ord(v) - ord('A')
    w = int(w)
    matrix[u][v] = w # Weight / Cost in case of edge
printmatrix(matrix)

def AIBFS(graph, start, visited, path):
    queue = deque()
    path.append(start)
    queue.append(start)

    visited[start] = True
    while len(queue) != 0:
        tempNode = queue.popleft()
        for neighbour in graph[tempNode]:
            if visited[neighbour] == False:
                path.append(neighbour)
                queue.append(neighbour)
                visited[neighbour] = True
    return path

graph = defaultdict(list)
v,e = map(int,input().split())
for i in range(e):
    u,v = map(str,input().split())
    graph[u].append(v)
    graph[v].append(u)

start = 'A'
path = []
visited = defaultdict(bool)
traversedPath = AIBFS(graph, start, visited, path)
print(traversedPath)