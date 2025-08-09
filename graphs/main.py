from bfs import single_source_bfs
from dfs import dfs
from graph import Graph, Node
from topological_sort import dfs_topo, khan, find_all_topological_orderings
from spp import bellman_ford, dijkstra, dijkstra_sspp
from mst import MST

if __name__ == "__main__":
    kigali = Node("Kigali")
    barcelona = Node("Barcelona")
    zanzibar = Node("Zanzibar")
    london = Node("London")
    tokyo = Node("Tokyo")
    amsterdam = Node("Amsterdam")
    ibiza = Node("Ibiza")
    marakech = Node("Marakesh")

    nodes = [kigali, barcelona, zanzibar, london, tokyo, amsterdam, ibiza, marakech]

    # Undirected graph (for BFS, DFS, Dijkstra)
    undirected_graph = Graph(directed=False)
    for node in nodes:
        undirected_graph.add_node(node)

    undirected_graph.add_edge(kigali, barcelona, 4)
    undirected_graph.add_edge(kigali, zanzibar, 2)
    undirected_graph.add_edge(london, amsterdam, 1)
    undirected_graph.add_edge(ibiza, marakech, 7)
    undirected_graph.add_edge(tokyo, barcelona, 3)
    undirected_graph.add_edge(marakech, amsterdam, 2)
    undirected_graph.add_edge(london, tokyo, 6)
    undirected_graph.add_edge(ibiza, tokyo, 5)

    print("Undirected graph loaded with nodes and edges.")

    bfs_result = single_source_bfs(undirected_graph, kigali)
    print("BFS traversal:", bfs_result)

    print("\nDFS traversal output:")
    dfs(undirected_graph)

    print("\nDijkstra's shortest path")
    dijkstra_sspp(undirected_graph, kigali)

    print("\nBellman Ford's shortest path from Kigali")
    bellman_ford(undirected_graph, kigali)

    negative_graph = undirected_graph
    negative_graph.add_edge(tokyo, zanzibar, 4)
    print("\nBellman Ford's shortest path from Kigali (with negative weights)")
    bellman_ford(undirected_graph, kigali)

    # Directed graph (for topological sorts)
    directed_graph = Graph(directed=True)
    for node in nodes:
        directed_graph.add_node(node)

    directed_graph.add_edge(kigali, barcelona, 4)
    directed_graph.add_edge(kigali, zanzibar, 2)
    directed_graph.add_edge(london, amsterdam, 1)
    directed_graph.add_edge(ibiza, marakech, 7)
    directed_graph.add_edge(tokyo, barcelona, 3)
    directed_graph.add_edge(marakech, amsterdam, 2)
    directed_graph.add_edge(london, tokyo, 6)
    directed_graph.add_edge(ibiza, tokyo, 5)

    print("\nDirected graph loaded with nodes and edges.")

    print("\nTopological sorts:")
    dfs_topo(directed_graph)
    khan(directed_graph)
    find_all_topological_orderings(directed_graph)

    print("\nTopological sorts:")
    dfs_topo(directed_graph)
    khan(directed_graph)
    find_all_topological_orderings(directed_graph)

    print("\nPrim's MST:")

    # Add edges to fully connect the graph so we can find the MST
    undirected_graph.add_edge(zanzibar, london, 3)
    undirected_graph.add_edge(amsterdam, ibiza, 4)

    mst = MST(undirected_graph)
    cost, edges = mst.prims(kigali)
    cost, edges = mst.eager_prims(kigali)
