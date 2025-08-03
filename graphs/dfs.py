from typing import List
from collections import defaultdict


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.parent = None
        self.color = None
        self.discovery_time = 0
        self.finish_time = 0

    def __repr__(self):
        return self.value


class Graph:
    def __init__(self) -> None:
        self.nodes = set()
        self.relationships = defaultdict(set)
        self.time = 0
        self.topological_sort_list = []

    def add_node(self, node) -> None:
        self.nodes.add(node)

    def add_edges(self, node1: Node, node2: Node) -> None:
        self.relationships[node1].add(node2)
        self.relationships[node2].add(node1)

    def get_neighbors(self, node: Node) -> List[Node]:
        return self.relationships[node]

    def dfs(self):

        for node in self.nodes:
            node.color = "WHITE"
            node.parent = None

        self.time = 0

        for node in self.nodes:
            if node.color == "WHITE":
                self.dfs_visit(node)

        print("\n-------------------------------\n")
        for x in self.nodes:
            print(self.time, x, x.color, x.discovery_time, x.finish_time)
        print("\n-------------------------------\n")

    def dfs_visit(self, node: Node):

        # Print status
        for x in self.nodes:
            print(self.time, x, x.color, x.discovery_time, x.finish_time)
        print("\n")
        self.time += 1
        node.discovery_time = self.time
        node.color = "GRAY"

        for neighbor in self.get_neighbors(node):
            if neighbor.color == "WHITE":
                neighbor.parent = node
                self.dfs_visit(neighbor)

        node.color = "BLACK"
        self.time += 1
        node.finish_time = self.time
        self.topological_sort_list.append(node)


kigali = Node("Kigali")
barcelona = Node("Barcelona")
zanzibar = Node("Zanzibar")
london = Node("London")
tokyo = Node("Tokyo")
amsterdam = Node("Amsterdam")
ibiza = Node("Ibiza")
marakech = Node("marakesh")

nodes = [kigali, barcelona, zanzibar, london, tokyo, amsterdam, ibiza, marakech]
graph = Graph()

for node in nodes:
    graph.add_node(node)

graph.add_edges(kigali, barcelona)
graph.add_edges(kigali, zanzibar)
graph.add_edges(london, amsterdam)
graph.add_edges(ibiza, marakech)
graph.add_edges(tokyo, barcelona)
graph.add_edges(marakech, amsterdam)
graph.add_edges(london, tokyo)
graph.add_edges(ibiza, tokyo)

"""
       Zanzibar
           |
        Kigali
           |
      Barcelona
           |
         Tokyo
        /     \
     London   Ibiza
        |       |
    Amsterdam marakesh
        \       /
         -------

"""

print(graph.get_neighbors(kigali))
print(graph.get_neighbors(tokyo))
print(graph.get_neighbors(ibiza))

graph.dfs()
