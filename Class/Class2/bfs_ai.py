adjacency_dictionary = {'A':['B', 'C', 'D', 'E'], 'B':['A', 'C'],
'C':['B', 'A', 'D'], 'D':['A', 'C'], 'E':['A']}

print(adjacency_dictionary.keys())

print(adjacency_dictionary['A'])

my_dictionary = {'A':['C', 'B'], 'C':['A'], 'B':['A']}
graph = Graph(my_dictionary)
print(graph)
