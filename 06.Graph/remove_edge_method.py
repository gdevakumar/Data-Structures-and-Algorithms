from graph import Graph

my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')

my_graph.add_edge('A','B')
my_graph.add_edge('B','C')
my_graph.add_edge('C','A')

print('Graph before remove_edge():')
my_graph.print()


my_graph.remove_edge('A','C')


print('\nGraph after remove_edge():')
my_graph.print()