# Undirected Graph
~~~~ Python
import matplotlib.pyplot as plt
import networkx as nx

# Create a new graph
G = nx.Graph()

# Add nodes
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_node('E')

# Add edges
G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_edge('A', 'D')
G.add_edge('B', 'C')
G.add_edge('B', 'D')
G.add_edge('C', 'D')
G.add_edge('D', 'E')

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_size=2000, node_color="skyblue", font_size=20, font_weight="bold")
plt.title("Graph Visualization")
plt.show()
~~~~

# Directed Graph

~~~~ Python
# Create a new directed graph
DG = nx.DiGraph()

# Add nodes
DG.add_nodes_from(['A', 'B', 'C', 'D', 'E'])

# Add directed edges
DG.add_edge('A', 'B')
DG.add_edge('A', 'C')
DG.add_edge('B', 'D')
DG.add_edge('D', 'E')
DG.add_edge('C', 'D')

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(DG, with_labels=True, node_size=2000, node_color="lightgreen", font_size=20, font_weight="bold", arrows=True, arrowsize=20)
plt.title("Directed Graph Visualization")
plt.show()
~~~~

# No Simple Graph

~~~~ Python
# Create a new directed graph for the specified structure
DG2 = nx.MultiDiGraph()

# Add nodes
DG2.add_nodes_from(['A', 'B', 'C'])

# Add directed edges, including double edges and a self-loop
DG2.add_edge('A', 'B') # First edge A -> B
DG2.add_edge('B', 'A') # B -> A
DG2.add_edge('A', 'B') # Second edge A -> B (creating a double edge)
DG2.add_edge('C', 'C') # Self-loop at C

# Draw the graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(DG2) # Position nodes using the spring layout
nx.draw(DG2, pos, with_labels=True, node_size=2000, node_color="orange", font_size=20, font_weight="bold", arrows=True, arrowsize=20)
nx.draw_networkx_edge_labels(DG2, pos, edge_labels={('A', 'B'): 'Double Edge', ('C', 'C'): 'Self-loop'}, font_color='red')
plt.title("Directed Graph with Double Edges and Self-Loop")
plt.show()
~~~~

# Weighted Graph

~~~~ python
# Create a new directed graph for the specified weighted structure
WG = nx.DiGraph()

# Add nodes
WG.add_nodes_from(['A', 'B', 'C', 'D'])

# Add weighted directed edges
WG.add_edge('A', 'B', weight=5)
WG.add_edge('A', 'C', weight=3)
WG.add_edge('B', 'D', weight=2)
WG.add_edge('C', 'D', weight=1)

# Draw the graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(WG) # Position nodes using the spring layout
nx.draw(WG, pos, with_labels=True, node_size=2000, node_color="lightpink", font_size=20, font_weight="bold", arrows=True, arrowsize=20)

# Draw edge labels (weights)
edge_labels = nx.get_edge_attributes(WG, 'weight')
nx.draw_networkx_edge_labels(WG, pos, edge_labels=edge_labels)

plt.title("Weighted Directed Graph")
plt.show()

~~~~

# Completed Graph
~~~~~Python
# Re-import necessary libraries and re-create the complete graph after a reset
import matplotlib.pyplot as plt
import networkx as nx

# Create a new graph for a complete network (every node is connected to every other node)
CG = nx.complete_graph(4)

# Relabel nodes from 0, 1, 2, 3 to A, B, C, D
CG = nx.relabel_nodes(CG, {0: 'A', 1: 'B', 2: 'C', 3: 'D'})

# Draw the complete graph
plt.figure(figsize=(8, 6))
nx.draw(CG, with_labels=True, node_size=2000, node_color="lightblue", font_size=20, font_weight="bold", edge_color="gray")
plt.title("Complete Graph Visualization")
plt.show()
~~~~~

