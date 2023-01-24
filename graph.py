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



import networkx as nx

def a_star(graph, start, goal):
    frontier = [(start, 0)]
    visited = set()
    while frontier:
        current = frontier.pop(0)
        if current[0] in visited:
            continue
        print("Expanding node:", current[0])
        visited.add(current[0])
        if current[0] == goal:
            return current[1]
        for neighbor in graph[current[0]]:
            #calculate the cost to move to the neighbor node
            cost = graph[current[0]][neighbor]['weight']
            # calculate the heuristic value (estimated cost to reach the goal)
            heuristic = abs(neighbor - goal)
            # add the neighbor node to the frontier with the total cost
            frontier.append((neighbor, current[1] + cost + heuristic))
            print("Crossing node:", neighbor)
        frontier = sorted(frontier, key=lambda x: x[1])

# create the graph
G = nx.Graph()
G.add_edge(1, 2, weight=1)
G.add_edge(1, 3, weight=4)
G.add_edge(2, 4, weight=2)
G.add_edge(3, 4, weight=1)
G.add_edge(4, 5, weight=3)
G.add_edge(4, 6, weight=5)
G.add_edge(5, 6, weight=1)
 
# plot the graph
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
plt.show()
 
# perform A* search
result = a_star(G, 1, 6)
print("Shortest path cost:", result)