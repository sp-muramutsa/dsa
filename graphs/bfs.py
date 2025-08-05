from collections import deque
from typing import List
from graph import Node, Graph


def single_source_bfs(graph: Graph, source: Node) -> List[Node]:
    """
    BFS from a given source node
    """

    traversal = []

    q = deque([source])
    source.visited = True

    while q:
        curr = q.popleft()
        traversal.append(curr)

        for neighbor in graph.get_neighbors(curr):
            if not neighbor.visited:
                neighbor.visited = True
                q.append(neighbor)

    graph.reset_visitation()
    return traversal
