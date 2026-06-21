import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Node:
    id: str
    name: str

@dataclass
class Diagram:
    nodes: List[Node]
    edges: List[Dict[str, str]]

class SystemSculptor:
    def __init__(self):
        self.project_session = {}

    def load_diagram(self, mermaid_source: str) -> Diagram:
        # Simplified Mermaid source parsing for demonstration purposes
        nodes = []
        edges = []
        for line in mermaid_source.splitlines():
            if line.startswith("node"):
                node_id, node_name = line.split()[1], line.split()[2]
                nodes.append(Node(node_id, node_name))
            elif line.startswith("edge"):
                edge_from, edge_to = line.split()[1], line.split()[2]
                edges.append({"from": edge_from, "to": edge_to})
        return Diagram(nodes, edges)

    def add_node(self, diagram: Diagram, node_id: str, node_name: str) -> Diagram:
        diagram.nodes.append(Node(node_id, node_name))
        return diagram

    def remove_node(self, diagram: Diagram, node_id: str) -> Diagram:
        diagram.nodes = [node for node in diagram.nodes if node.id != node_id]
        diagram.edges = [edge for edge in diagram.edges if edge["from"] != node_id and edge["to"] != node_id]
        return diagram

    def rename_node(self, diagram: Diagram, node_id: str, new_name: str) -> Diagram:
        for node in diagram.nodes:
            if node.id == node_id:
                node.name = new_name
                break
        return diagram

    def save_diagram(self, diagram: Diagram) -> None:
        self.project_session["diagram"] = {
            "nodes": [{"id": node.id, "name": node.name} for node in diagram.nodes],
            "edges": [{"from": edge["from"], "to": edge["to"]} for edge in diagram.edges]
        }

    def export_diagram(self) -> str:
        diagram = self.project_session.get("diagram")
        if diagram:
            mermaid_source = ""
            for node in diagram["nodes"]:
                mermaid_source += f"node {node['id']} {node['name']}\n"
            for edge in diagram["edges"]:
                mermaid_source += f"edge {edge['from']} {edge['to']}\n"
            return mermaid_source
        return ""
