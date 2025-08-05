from typing import List
from graph import Node, Graph


def dfs(graph: Graph) -> None:
    """
    Perform DFS on the given graph and print discovery and finishing times.
    """

    for node in graph.nodes:
        node.color = "WHITE"
        node.parent = None

    time = 0

    def dfs_visit(node: Node):
        nonlocal time
        time += 1
        node.discovery_time = time
        node.color = "GRAY"

        for neighbor in graph.get_neighbors(node):
            if neighbor.color == "WHITE":
                neighbor.parent = node
                dfs_visit(neighbor)

        node.color = "BLACK"
        time += 1
        node.finish_time = time

    for node in graph.nodes:
        if node.color == "WHITE":
            dfs_visit(node)

    print("\n--- DFS Result ---")
    for node in graph.nodes:
        print(f"{node}: discovery={node.discovery_time}, finish={node.finish_time}")
