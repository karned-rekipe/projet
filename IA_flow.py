from diagrams import Diagram, Cluster
from diagrams.onprem.queue import Kafka
from diagrams.onprem.compute import Server
from diagrams.programming.language import Python

with Diagram("Architecture Kafka & FastAPI", direction="TB", show=False):
    # Espaceur invisible
    spacer = Server(" ")

    # Regrouper les APIs FastAPI
    with Cluster("APIs FastAPI"):
        app = Server("App")
        artefact_storage = Server("Artefact Storage")
        data_storage = Server("Data Storage")
        extract_data = Server("Extract Data")

    spacer  # Ajout d'un espace visuel

    # Regrouper les topics Kafka
    with Cluster("Topics Kafka"):
        artefact_topic = Kafka("Artefact Storage Topic")
        extract_topic = Kafka("Extract Data Topic")

    spacer  # Ajout d'un espace visuel

    # Regrouper les Consumers Kafka
    with Cluster("Consumers Kafka"):
        consumer_artefact_1 = Python("Consumer -> Data Storage")
        consumer_artefact_2 = Python("Consumer -> Extract Data")
        consumer_extract = Python("Consumer -> Data Storage (Extract)")

    # Flux des appels API et Kafka
    app >> artefact_storage
    artefact_storage >> artefact_topic
    artefact_topic >> consumer_artefact_1 >> data_storage
    artefact_topic >> consumer_artefact_2 >> extract_data
    extract_data >> extract_topic
    extract_topic >> consumer_extract >> data_storage