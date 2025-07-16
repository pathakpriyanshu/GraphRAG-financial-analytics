import pandas as pd
import networkx as nx
from pyvis.network import Network

# --- load parquet files ---
entities   = pd.read_parquet(r"D:\1. INDIUM\Project\DATA\graphrag\output\entities.parquet")
relations  = pd.read_parquet(r"D:\1. INDIUM\Project\DATA\graphrag\output\relationships.parquet")

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