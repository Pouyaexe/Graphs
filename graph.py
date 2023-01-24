import networkx as nx

G = nx.Graph()

# add vertices and edges to the graph
A, B, C, D, E, F, Gn, H, I, J, K, L, M = range(1, 14)

# or we can use dictionary to store the vertices and their weights A's weight is 10, B's weight is 1, etc.
vertices = {A: 10, B: 1, C: 20, D: 1, E: 17, F: 11, Gn: 6, H: 1, I: 9, J: 8, K: 6, L: 5, M: 1}
vertices_weights = {1: 10, 2: 1, 3: 20, 4: 1, 5: 17, 6: 11, 7: 6, 8: 1, 9: 9, 10: 8, 11: 6, 12: 5, 13: 1}

G.add_edge(A, B, weight=2)
G.add_edge(A, C, weight=15)
G.add_edge(A, D, weight=3)

G.add_edge(B, E, weight=7)
G.add_edge(B, F, weight=11)

G.add_edge(D, Gn, weight=22)
G.add_edge(D, H, weight=5)

G.add_edge(F, I, weight=5)
G.add_edge(F, J, weight=3)
G.add_edge(F, K, weight=6)

G.add_edge(H, L, weight=5)
G.add_edge(H, M, weight=1) # traget is M

# set vertex weights using dictionary vertices_weights
#Print the graph vertices and edges and their weights


import matplotlib.pyplot as plt

# draw the graph with labels and weights on edges 
print('G: ', G.edges(data=True))
nx.draw(G, with_labels=True, font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'weight')
print('edge_labels: ', edge_labels)
nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G), edge_labels=edge_labels)
# Weights are all over the place, so we need to adjust the position of the labels to make them readable
edge_labels_pos = {(1, 2): (0.5, 0.5), (1, 3): (0.5, 0.5), (1, 4): (0.5, 0.5), (2, 5): (0.5, 0.5), (2, 6): (0.5, 0.5), (4, 7): (0.5, 0.5), (4, 8): (0.5, 0.5), (6, 9): (0.5, 0.5), (6, 10): (0.5, 0.5), (6, 11): (0.5, 0.5), (8, 12): (0.5, 0.5), (8, 13): (0.5, 0.5)}
nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G), edge_labels=edge_labels, label_pos=edge_labels_pos)

# show the graph
plt.show()
