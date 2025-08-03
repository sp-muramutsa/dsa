from bfs import Node, Graph


class UnionFind:
    def __init__(self, nodes):
        self.parents = {node: node for node in nodes}
        self.ranks = {node: 0 for node in nodes}
        self.sizes = {node: 1 for node in nodes}

    def find(self, child: Node) -> Node:

        # Element is its own parent
        if self.parents[child] == child:
            return child

        # Recursively go up the family tree
        return self.find(self.parents[child])

    def union(self, node1: Node, node2: Node) -> None:

        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 != parent2:
            self.parents[parent1] = parent2

    """
    Optimized Methods for Union & Find
    """

    def find_with_path_compression(self, child: Node) -> Node:

        # Set child's parent to the eldest ancestor
        if self.parents[child] != child:
            self.parents[child] = self.find_with_path_compression(self.parents[child])

        return self.parents[child]

    def union_with_rank(self, node1: Node, node2: Node) -> None:

        parent1 = self.find_with_path_compression(node1)
        parent2 = self.find_with_path_compression(node2)

        if parent1 == parent2:
            return

        # Prefer the taller parent to stay as parent
        if self.ranks[parent1] < self.ranks[parent2]:
            self.parents[parent1] = parent2
        elif self.ranks[parent1] > self.ranks[parent2]:
            self.parents[parent2] = parent1
        else:
            self.parents[parent2] = parent1
            self.ranks[parent1] += 1  # Increase rank of the new parent

    def union_with_size(self, node1: Node, node2: Node) -> None:

        parent1 = self.find_with_path_compression(node1)
        parent2 = self.find_with_path_compression(node2)

        if parent1 == parent2:
            return

        # Prefer the bigger parent to stay a parent
        if self.sizes[parent1] > self.sizes[parent2]:
            self.parents[parent2] = parent1
            self.sizes[parent1] += self.sizes[parent2]

        else:
            self.parents[parent1] = parent2
            self.sizes[parent2] += self.sizes[parent1]


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

uf = UnionFind(nodes)

# uf.union(kigali, barcelona)
# print(uf.find(barcelona))
# print(uf.find(kigali))

# uf.union(london, zanzibar)
# print("\n")
# print(uf.find(london))
# print(uf.find(zanzibar))

# uf.union(kigali, london)
# print("\n")
# print(uf.find(barcelona))
# print(uf.find(kigali))
# print(uf.find(london))
# print(uf.find(zanzibar))


# uf.union_with_rank(kigali, barcelona)
# print(uf.find_with_path_compression(barcelona))
# print(uf.find_with_path_compression(kigali))

# uf.union_with_rank(london, zanzibar)
# print("\n")
# # print(uf.find_with_path_compression(london))
# # print(uf.find_with_path_compression(zanzibar))

# # uf.union_with_rank(kigali, london)
# # print("\n")
# # print(uf.find_with_path_compression(barcelona))
# # print(uf.find_with_path_compression(kigali))
# # print(uf.find_with_path_compression(london))
# # print(uf.find_with_path_compression(zanzibar))


uf.union_with_size(london, barcelona)
uf.union_with_size(kigali, london)
uf.union_with_size(london, zanzibar)
uf.union_with_size(ibiza, zanzibar)

print("\n")
print(uf.find_with_path_compression(barcelona))
print(uf.find_with_path_compression(kigali))
print(uf.find_with_path_compression(london))
print(uf.find_with_path_compression(zanzibar))
print(uf.find_with_path_compression(ibiza))
