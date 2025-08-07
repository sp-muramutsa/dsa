import heapq
from graph import Node


class MST:
    """
    Minimum cost Spanning Tree of a graph
    """

    def __init__(self, graph):
        self.graph = graph

    def heappush_edges(self, src: Node, heap: list, visited_nodes: set) -> None:
        """
        Add all nodes that point to unvisited nodes
        """

        visited_nodes.add(src)

        for dest in self.graph.edges[src]:
            if dest not in visited_nodes:
                heapq.heappush(heap, (self.graph.costs[(src, dest)], src, dest))

    def prims(self, source: Node):
        """
        Lazy Prim's Algorithm for finding the MST of a graph
        """

        n = len(self.graph.nodes)
        m = n - 1

        edge_count = 0
        mst_cost = 0

        mst_edges = []
        visited_nodes = set()

        heap = []

        # Mark source as visited
        visited_nodes.add(source)

        # Add all edges that the source points to
        self.heappush_edges(source, heap, visited_nodes)

        while heap and edge_count < m:

            cost, src, dest = heapq.heappop(heap)

            if dest in visited_nodes:
                continue

            mst_edges.append((src, dest, cost))
            edge_count += 1
            mst_cost += cost

            self.heappush_edges(dest, heap, visited_nodes)

        print("MST cost: ", mst_cost)
        print("MST edges in order; ", mst_edges)
        if edge_count != m:
            print("No MST found")
            return (None, None)

        return (mst_cost, mst_edges)

    def kruskals(self):
        pass
