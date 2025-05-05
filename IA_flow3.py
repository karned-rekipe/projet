import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

# Ajouter des nœuds
nodes = ["App", "Artefact Storage", "Artefact Storage Topic", "Consumer -> Data Storage",
         "Consumer -> Extract Data", "Extract Data", "Extract Data Topic", "Data Storage"]
G.add_nodes_from(nodes)

# Ajouter des arêtes
edges = [("App", "Artefact Storage"), ("Artefact Storage", "Artefact Storage Topic"),
         ("Artefact Storage Topic", "Consumer -> Data Storage"),
         ("Artefact Storage Topic", "Consumer -> Extract Data"),
         ("Consumer -> Extract Data", "Extract Data"),
         ("Extract Data", "Extract Data Topic"),
         ("Extract Data Topic", "Consumer -> Data Storage"),
         ("Consumer -> Data Storage", "Data Storage")]
G.add_edges_from(edges)

# Dessiner le graphe
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G)  # Layout automatique
nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=3000, font_size=10)
plt.show()