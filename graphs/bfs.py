from collections import deque, defaultdict
from typing import List


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.visited = False
        self.in_degree = 0

    def __repr__(self):
        return self.value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return isinstance(other, Node) and self.value == other.value


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

    def reset_visitation(self):
        for node in self.nodes:
            node.visited = False

    def single_source_bfs(self, source: Node) -> None:
        """
        BFS from a given source node
        """

        traversal = []

        q = deque([source])
        source.visited = True

        while q:
            curr = q.popleft()
            traversal.append(curr)

            for neighbor in self.get_neighbors(curr):
                if not neighbor.visited:
                    neighbor.visited = True
                    q.append(neighbor)

        print(traversal)
        self.reset_visitation()


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

# graph.single_source_bfs(kigali)
# graph.single_source_bfs(london)
