from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.database import Mongodb
from diagrams.onprem.network import Nginx
from diagrams.programming.framework import FastAPI, React

graph_attr = {
    "layout": "dot",
    "rankdir": "LR",
    "nodesep": "1",
    "ranksep": "1",
    "splines": "true",
    "ratio": "0.5",
}

node_attr = {
    "fontcolor": "black",
    "fontsize": "16",
    "shape": "ellipse",
    "style": "transparent",
    "color": "black"
}

edge_attr = {
    "color": "black",
    "arrowhead": "normal",
    "fontcolor": "black"
}

with (Diagram("Karned", show = False, graph_attr = graph_attr, node_attr = node_attr, edge_attr = edge_attr)) as diag:
    with Cluster("Gateway"):
        gateway = Nginx("gateway")

    with Cluster("APP"):
        app_recipe = React("recipe")
        app_ingredient = React("ingredient")
        app_planning = React("planning")
        app_shopping = React("shopping")

    with Cluster("API"):
        with Cluster("API Recipe"):
            api_recipe = FastAPI("recipe")
            db_recipe = Mongodb("recipe")

        with Cluster("API Ingredient"):
            api_ingredient = FastAPI("ingredient")
            db_ingredient = Mongodb("ingredient")

        with Cluster("API Planning"):
            api_planning = FastAPI("planning")
            db_planning = Mongodb("planning")

        with Cluster("API Shopping"):
            api_shopping = FastAPI("shopping")
            db_shopping = Mongodb("shopping")

    app_recipe >> Edge() << gateway >> Edge() << api_recipe >> Edge() << db_recipe
    app_ingredient >> Edge() << gateway >> Edge() << api_ingredient >> Edge() << db_ingredient
    app_planning >> Edge() << gateway >> Edge() << api_planning >> Edge() << db_planning
    app_shopping >> Edge() << gateway >> Edge() << api_shopping >> Edge() << db_shopping