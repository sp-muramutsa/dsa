import heapq


def dijkstra(graph):
    for node in graph.nodes:
        dists = single_source_shortest_path(graph, node)
        for destination, distance in dists.items():
            print(f"{node} -> {destination}: {distance}")
        print("\n")


def single_source_shortest_path(graph, source):
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

    return distances
