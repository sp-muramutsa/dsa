from collections import deque, defaultdict
from typing import List, Dict, Tuple
import heapq


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.distance = 0
        self.cost = 0

    def __repr__(self):
        return self.value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return isinstance(other, Node) and self.value == other.value
    
    def __lt__(self ,other):
        return self.value < other.value


class Graph:
    def __init__(self) -> None:
        self.nodes: List[Node] = []
        self.edges: Dict[Node, List[Node]] = {}
        self.costs: Dict[Tuple[Node, Node], int] = {}

    def add_node(self, node: Node) -> None:
        self.nodes.append(node)
        self.edges[node] = []

    def add_edge(self, node1: Node, node2: Node, cost: int) -> None:

        self.edges[node1].append(node2)
        self.edges[node2].append(node1)

        self.costs[(node1, node2)] = cost
        self.costs[(node2, node1)] = cost

    def get_neighbors(self, node: Node) -> List[Node]:
        return self.edges[node]

    def get_cost(self, node1: Node, node2: Node) -> int:
        return self.costs[(node1, node2)]

    def dijkstra(self):
        for node in self.nodes:
            dists = self.single_source_shortest_path(node)
            for destination, distance in dists.items():
                print(f"{node} -> {destination}: {distance}")
            print("\n")

    def single_source_shortest_path(self, source):

        distances = {node: float("inf") for node in self.nodes}
        visited = set()
        distances[source] = 0

        heap = []
        heapq.heappush(heap, (0, source))

        while heap:
            du, curr = heapq.heappop(heap)
            if curr in visited:
                continue
            visited.add(curr)

            for neighbor in self.get_neighbors(curr):

                cost = self.costs[(curr, neighbor)]
                new_dist = du + cost
                dv = distances[neighbor]

                if new_dist < dv:
                    distances[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

        return distances


kigali = Node("Kigali")
barcelona = Node("Barcelona")
zanzibar = Node("Zanzibar")
london = Node("London")
tokyo = Node("Tokyo")
amsterdam = Node("Amsterdam")
ibiza = Node("Ibiza")
marakech = Node("Marakesh")

nodes = [kigali, barcelona, zanzibar, london, tokyo, amsterdam, ibiza, marakech]
graph = Graph()

for node in nodes:
    graph.add_node(node)

# Add edges with cost
graph.add_edge(kigali, barcelona, 4)
graph.add_edge(kigali, zanzibar, 2)
graph.add_edge(london, amsterdam, 1)
graph.add_edge(ibiza, marakech, 7)
graph.add_edge(tokyo, barcelona, 3)
graph.add_edge(marakech, amsterdam, 2)
graph.add_edge(london, tokyo, 6)
graph.add_edge(ibiza, tokyo, 5)

graph.dijkstra()
