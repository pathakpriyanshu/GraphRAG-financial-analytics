import pandas as pd
import networkx as nx
from pyvis.network import Network

# --- load parquet files ---
entities   = pd.read_parquet("Path_of_enitites_parquet_files")
relations  = pd.read_parquet("Path_of_realtions_parquet_files")

# --- build graph ---
G = nx.Graph()
for _, row in entities.iterrows():
    G.add_node(row["id"],
               label=row.get("name", row["id"]),
               title=row.get("type", "Entity"))

for _, row in relations.iterrows():
    G.add_edge(row["source"], row["target"],
               title=row.get("predicate", "related to"))

# --- visualise ---
net = Network(height="800px", width="100%")   # notebook=False by default
net.from_nx(G)
net.show("graphrag_visualization.html", notebook=False)

print("✅ Open 'graphrag_visualization.html' in your browser.")
