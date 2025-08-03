from typing import List
from collections import defaultdict, deque


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.visited = False
        self.in_degree = 0

    def __repr__(self):
        return self.value


class DAG:
    def __init__(self) -> None:
        self.nodes = defaultdict(set)
        self.topological_ordering = deque()
        self.all_topological_orderings = []
        self.khan_topological_ordering = []

    def add_node(self, node) -> None:
        self.nodes[node] = set()

    def add_directed_edge(self, source: Node, destination: Node) -> None:
        destination.in_degree += 1
        self.nodes[source].add(destination)

    def get_neighbors(self, node: Node) -> List[Node]:
        return self.nodes[node]

    def reset_visitation(self):
        for node in self.nodes:
            node.visited = False

    def topological_sort(self):

        for node in self.nodes:
            if not node.visited:
                self.dfs(node)
        print(self.topological_ordering)

    def dfs(self, node: Node):
        node.visited = True
        for neighbor in self.get_neighbors(node):
            if not neighbor.visited:
                self.dfs(neighbor)
        self.topological_ordering.appendleft(node)

    def khan(self):
        """
        Implementation of Khan's alogrithm to find a valid topological ordering of a directed graph or to detect a cyle if any is present.
        """

        q = deque()
        for node in self.nodes:
            if node.in_degree == 0:
                q.append(node)

        while q:

            # Process front node
            curr = q.popleft()
            self.khan_topological_ordering.append(curr)
            curr.visited = True

            # Reduce in degree of neighobrs
            for neighbor in self.get_neighbors(curr):
                neighbor.in_degree -= 1

                # Push ready nodes to the queue
                if neighbor.in_degree == 0 and not neighbor.visited:
                    q.append(neighbor)

        # Detect cyle
        for node in self.nodes:
            if not node.visited:
                print("Graph is cyclic. No valid topological ordering.")
                self.khan_topological_ordering = []
                return

        print(self.khan_topological_ordering)

    def find_all_topological_orderings(self, path):
        """
        Uses backtracking to print all valid topological orderings of a DAG.
        """

        if len(path) == len(self.nodes):
            # print(path)
            self.all_topological_orderings.append(path[:])
            return

        for node in self.nodes:

            if node.in_degree == 0 and not node.visited:

                # Visit node
                for neighbor in self.get_neighbors(node):
                    neighbor.in_degree -= 1
                path.append(node)
                node.visited = True

                # Recur
                self.find_all_topological_orderings(path)

                # Backtrack i.e. reset
                for neighbor in self.get_neighbors(node):
                    neighbor.in_degree += 1
                path.pop()
                node.visited = False


kigali = Node("Kigali")
barcelona = Node("Barcelona")
zanzibar = Node("Zanzibar")
london = Node("London")
tokyo = Node("Tokyo")
amsterdam = Node("Amsterdam")
ibiza = Node("Ibiza")
marakech = Node("Marakesh")

nodes = [kigali, barcelona, zanzibar, london, tokyo, amsterdam, ibiza, marakech]
graph = DAG()

for node in nodes:
    graph.add_node(node)

graph.add_directed_edge(kigali, barcelona)
graph.add_directed_edge(kigali, zanzibar)
graph.add_directed_edge(london, amsterdam)
graph.add_directed_edge(ibiza, marakech)
graph.add_directed_edge(tokyo, barcelona)
graph.add_directed_edge(marakech, amsterdam)
graph.add_directed_edge(london, tokyo)
graph.add_directed_edge(ibiza, tokyo)

"""

Kigali -> Barcelona  <-  Tokyo
       -> Zanzibar       * *
       ------------------  |
     /                     |
London -> Amsterdam        |
           |               |
Ibiza -> Marakech          |
|---------------------------
"""

graph.topological_sort()
graph.reset_visitation()
graph.find_all_topological_orderings([])
print(f"\nTotal topological orderings: {len(graph.all_topological_orderings)}")
graph.reset_visitation()

graph.khan()
