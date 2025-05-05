from graphviz import Digraph

dot = Digraph("Kafka_FastAPI", format="png")

# Définition des clusters
with dot.subgraph(name="cluster_APIs") as c:
    c.attr(label="APIs FastAPI", style="filled", color="lightgrey")
    c.node("App")
    c.node("Artefact Storage")
    c.node("Data Storage")
    c.node("Extract Data")

with dot.subgraph(name="cluster_Topics") as c:
    c.attr(label="Kafka Topics", style="filled", color="lightblue")
    c.node("Artefact Storage Topic", shape="cylinder")
    c.node("Extract Data Topic", shape="cylinder")

with dot.subgraph(name="cluster_Consumers") as c:
    c.attr(label="Kafka Consumers", style="filled", color="lightyellow")
    c.node("Consumer -> Data Storage")
    c.node("Consumer -> Extract Data")
    c.node("Consumer -> Data Storage (Extract)")

# Connexions
dot.edge("App", "Artefact Storage")
dot.edge("Artefact Storage", "Artefact Storage Topic")
dot.edge("Artefact Storage Topic", "Consumer -> Data Storage")
dot.edge("Artefact Storage Topic", "Consumer -> Extract Data")
dot.edge("Consumer -> Extract Data", "Extract Data")
dot.edge("Extract Data", "Extract Data Topic")
dot.edge("Extract Data Topic", "Consumer -> Data Storage (Extract)")
dot.edge("Consumer -> Data Storage (Extract)", "Data Storage")

dot.render("kafka_fastapi_diagram", view=True)  # Génère et affiche le graph