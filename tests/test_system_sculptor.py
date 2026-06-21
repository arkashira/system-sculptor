import pytest
from system_sculptor import SystemSculptor, Diagram, Node

def test_load_diagram():
    sculptor = SystemSculptor()
    mermaid_source = "node A NodeA\nnode B NodeB\nedge A B"
    diagram = sculptor.load_diagram(mermaid_source)
    assert len(diagram.nodes) == 2
    assert len(diagram.edges) == 1

def test_add_node():
    sculptor = SystemSculptor()
    diagram = Diagram([Node("A", "NodeA")], [])
    updated_diagram = sculptor.add_node(diagram, "B", "NodeB")
    assert len(updated_diagram.nodes) == 2

def test_remove_node():
    sculptor = SystemSculptor()
    diagram = Diagram([Node("A", "NodeA"), Node("B", "NodeB")], [{"from": "A", "to": "B"}])
    updated_diagram = sculptor.remove_node(diagram, "B")
    assert len(updated_diagram.nodes) == 1
    assert len(updated_diagram.edges) == 0

def test_rename_node():
    sculptor = SystemSculptor()
    diagram = Diagram([Node("A", "NodeA")], [])
    updated_diagram = sculptor.rename_node(diagram, "A", "NewName")
    assert updated_diagram.nodes[0].name == "NewName"

def test_save_and_export_diagram():
    sculptor = SystemSculptor()
    diagram = Diagram([Node("A", "NodeA"), Node("B", "NodeB")], [{"from": "A", "to": "B"}])
    sculptor.save_diagram(diagram)
    exported_diagram = sculptor.export_diagram()
    assert "node A NodeA" in exported_diagram
    assert "node B NodeB" in exported_diagram
    assert "edge A B" in exported_diagram
