from collections import deque
from typing import List
from graph import Graph, Node  # Import your existing classes for typing, optional


def reset_visitation(graph: Graph):
    for node in graph.nodes:
        node.visited = False


def dfs_topo(graph: Graph):
    """
    DFS-based topological sort. Prints ordering.
    """
    ordering = deque()

    def dfs_visit(node: Node):
        node.visited = True
        for neighbor in graph.get_neighbors(node):
            if not neighbor.visited:
                dfs_visit(neighbor)
        ordering.appendleft(node)

    reset_visitation(graph)
    for node in graph.nodes:
        if not node.visited:
            dfs_visit(node)

    print("Topological ordering (DFS):", list(ordering))
    return ordering


def khan(graph: Graph):
    """
    Khan's algorithm for topological sorting.
    Prints ordering or detects cycle.
    """
    # Recompute in_degree for all nodes before starting
    for node in graph.nodes:
        node.in_degree = 0
    for node in graph.nodes:
        for neighbor in graph.get_neighbors(node):
            neighbor.in_degree += 1

    q = deque()
    for node in graph.nodes:
        if node.in_degree == 0:
            q.append(node)

    ordering = []
    reset_visitation(graph)

    while q:
        curr = q.popleft()
        ordering.append(curr)
        curr.visited = True

        for neighbor in graph.get_neighbors(curr):
            neighbor.in_degree -= 1
            if neighbor.in_degree == 0 and not neighbor.visited:
                q.append(neighbor)

    if len(ordering) != len(graph.nodes):
        print("Graph is cyclic. No valid topological ordering.")
        return []

    print("Topological ordering (Khan):", ordering)
    return ordering


def find_all_topological_orderings(graph: Graph):
    """
    Find and return all possible topological orderings via backtracking.
    """
    # Recompute in_degree for all nodes before starting
    for node in graph.nodes:
        node.in_degree = 0
    for node in graph.nodes:
        for neighbor in graph.get_neighbors(node):
            neighbor.in_degree += 1

    all_orderings = []

    def backtrack(path: List[Node]):
        if len(path) == len(graph.nodes):
            all_orderings.append(path[:])
            return

        for node in graph.nodes:
            if node.in_degree == 0 and not node.visited:
                for neighbor in graph.get_neighbors(node):
                    neighbor.in_degree -= 1
                path.append(node)
                node.visited = True

                backtrack(path)

                for neighbor in graph.get_neighbors(node):
                    neighbor.in_degree += 1
                path.pop()
                node.visited = False

    reset_visitation(graph)
    backtrack([])

    print(f"Total topological orderings: {len(all_orderings)}")
    # for ordering in all_orderings:
    #     print(ordering)
    return all_orderings
