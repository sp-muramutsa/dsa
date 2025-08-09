import heapq
from graph import Graph, Node
from typing import Dict


def dijkstra(graph: Graph) -> None:

    for node in graph.nodes:
        dists = dijkstra_sspp(graph, node)
        for destination, distance in dists.items():
            print(f"{node} -> {destination}: {distance}")
        print("\n")


def dijkstra_sspp(graph: Graph, source: Node) -> Dict[Node, int]:

    distances = {node: float("inf") for node in graph.nodes}
    visited = set()
    distances[source] = 0

    heap = []
    heapq.heappush(heap, (0, source))

    while heap:
        du, curr = heapq.heappop(heap)
        if curr in visited:
            continue
        visited.add(curr)

        for neighbor in graph.get_neighbors(curr):
            cost = graph.get_cost(curr, neighbor)
            new_dist = du + cost
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    print(distances)
    return distances


def bellman_ford(graph, source: Node) -> Dict[Node, int]:

    distances = {node: float("inf") for node in graph.nodes}
    distances[source] = 0
    n = len(graph.nodes) - 1

    # Relax all edges for |V| - 1 times
    for _ in range(n):
        for u in graph.edges:
            for v in graph.edges[u]:
                new_dist = distances[u] + graph.costs[(u, v)]
                if new_dist < distances[v]:
                    distances[v] = new_dist

    # Check for nodes stuck in a negative cycle
    for u in graph.edges:
        for v in graph.edges[u]:
            new_dist = distances[u] + graph.costs[(u, v)]
            if new_dist < distances[v]:
                distances[v] = float("-inf")

    print(distances)
    return distances
