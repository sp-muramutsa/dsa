# Node
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)

# Traversal: DFS Pre-order
def pre_order_traversal(node):
    if node is None:
        return
    print(node.data)
    for child in node.children:
        pre_order_traversal(child)

# Depth-first Search
def depth_first_search(node, target):
    if node is None:
        return False
    
    if node.data == target:
        return True
    
    for child in node.children:
        if depth_first_search(child, target):
            return True
    return False

# Insert node
def insert_node(root, node):
    if root is None:
        root = node
    else:
        root.children.append(node)

# Delete node
def delete_node(root, target):
    if root is None:
        return None
    root.children = [child for child in root.children if child.data != target]
    for child in root.children:
        delete_node(child, target)

# Tree Height
def tree_height(node):
    print("Checking node ", node.data)
    if node is None:
        return 0
    if not node.children:
        return 1
    return 1 + max(tree_height(child) for child in node.children)

    


root = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
j = Node("F")
k = Node("G")
h = Node("H")
i = Node("I")
g = Node("G")
k = Node("K")

root.add_child(b)
root.add_child(f)
b.add_child(c)
b.add_child(d)
b.add_child(e)
d.add_child(h)
d.add_child(i)
f.add_child(g)

print(tree_height(i))



