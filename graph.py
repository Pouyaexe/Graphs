import networkx as nx

G = nx.Graph()

# add vertices and edges to the graph
G.add_edge(1, 2, weight=5)
G.add_edge(2, 3, weight=3)
G.add_edge(3, 4, weight=7)
G.add_edge(4, 5, weight=2)

# set vertex weights
for vertex in G.nodes():
    G.nodes[vertex]['weight'] = 10

# access edges and vertices weight 
print(G[1][2]['weight'])
print(G.nodes[1]['weight'])


import matplotlib.pyplot as plt

# draw the graph with labels and weights on edges and vertices  
nx.draw(G, with_labels=True)

# show the graph
plt.show()