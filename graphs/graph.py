from collections import defaultdict
from typing import List, Dict, Tuple


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.visited = False
        self.in_degree = 0
        self.parent = None
        self.color = None
        self.discovery_time = 0
        self.finish_time = 0
        self.distance = float("inf")

    def __repr__(self):
        return self.value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return isinstance(other, Node) and self.value == other.value

    def __lt__(self, other):
        return self.value < other.value


class Graph:
    def __init__(self, directed=False) -> None:
        self.nodes: set[Node] = set()
        self.edges: Dict[Node, List[Node]] = defaultdict(list)
        self.costs: Dict[Tuple[Node, Node], int] = {}
        self.directed = directed

    def add_node(self, node: Node) -> None:
        self.nodes.add(node)
        if node not in self.edges:
            self.edges[node] = []

    def add_edge(self, node1: Node, node2: Node, cost: int = 1) -> None:
        self.edges[node1].append(node2)
        self.costs[(node1, node2)] = cost
        if not self.directed:
            self.edges[node2].append(node1)
            self.costs[(node2, node1)] = cost
        else:
            node2.in_degree += 1

    def get_neighbors(self, node: Node) -> List[Node]:
        return self.edges[node]

    def reset_visitation(self):
        for node in self.nodes:
            node.visited = False
            node.in_degree = 0
            node.parent = None
            node.color = None
            node.discovery_time = 0
            node.finish_time = 0
            node.distance = float("inf")
        for src, dest in self.costs:
            if self.directed:
                dest.in_degree += 1

    def get_cost(self, node1: Node, node2: Node) -> int:
        return self.costs.get((node1, node2), float("inf"))
