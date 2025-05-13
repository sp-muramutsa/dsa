# Binary Search Tree

class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

# INSERTING INTO A BST
# Time: O(height) height is O(log2(n+1))  or O(n) in case the tree is skewed i.e linked list.  
# Space: O(1)
# Recursive insert. 
# def insert(root, key):
#     if root is None:
#         return Node(key)
    
#     elif root.value == key:
#         return root
    
#     if root.value < key:
#         root.right = insert(root.right, key)
#     else:
#         root.left = insert(root.left, key)
#     return root


# Iterative insert
def insert(root, key):
    new_node = Node(key)

    if root is None:
        return new_node
    
    curr = root
    parent = root

    while curr:
        parent = curr
        if curr.value == key:
            return root
        elif curr.value > key:
            curr = curr.left
        else:
            curr = curr.right
        
    if parent.value > key:
        parent.left = new_node
    else:
        parent.right = new_node
    
    return root

# In-order: Left -> Root -> Right
def inorder(root):
    if root is None:
        return
    
    inorder(root.left)
    print(root.value, end = " --> ")
    inorder(root.right)

# SEARCHING IN A BST
# Time idem au insert
# Time: O(h)
# Space: O(h) because of the time required to store the recursion stack
# Recursive search
# def search(root, key):

#     # Base case: root is None or key is present at root
#     if root is None:
#         return False
#     elif root.value == key:
#         return True
    
#     # Recursive
#     elif root.value < key:
#         return search(root.right, key)
#     else:
#         return search(root.left, key)

# Iterative search
def search(root, key):
    if root is None:
        return False
    
    curr = root

    while curr:
        if curr.value == key:
            return True
        elif curr.value < key:
            curr = curr.right
        else:
            curr = curr.left
    
    return False

# DELETING FROM A BST
# Recursive delete
def delete(root, key):
    # Base Case
    if root is None:
        return  root
    
    # Recursive case: Traverse the tree to find what node to delete
    if root.value > key:
        root.left = delete(root.left, key)
    elif root.value < key:
        root.right = delete(root.right, key)
    
    # When it's the right node to delete
    else:
        # Case 1: leaf node
        if root.left is None and root.right is None:
            return None
        
        # Case 2: One child
        if root.left is None:
            return root.right
        
        if root.right is None:
            return root.left
        
        # Case 3: 2 children. The node is replaced by it's inorder successor(min to the right) or inorder predecessor(max to the left)
        # Using inorder successor(min to the right)
        # successor = get_inorder_successor(root.right)
        # root.value = successor.value
        # root.right = delete(root.right, successor.value)

        # Using inorder predecessor(max the left)
        predecessor = get_inorder_predecessor(root.left)
        root.value = predecessor.value
        root.left = delete(root.left, predecessor.value)

    return root

def height(root):
    if not root:
        return 0 
    
    left_height = height(root.left)
    right_height = height(root.right)

    return max(left_height, right_height) + 1


# Utility function to find inorder successor(min to the right)
def get_inorder_successor(node):
    while node.left is not None:
        node = node.left
    return node

# Utility function to find inorder predecessor(max to the left)
def get_inorder_predecessor(node):
    while node.right is not None:
        node = node.right
    return node

# Iterative
def print_level_order(root):
    h = height(root)
    for i in range(1, h+1):
        print_current_level(root, i)

def print_current_level(root, level):
    if root is None:
        return
    
    # Base case 
    if level == 1:
        print(root.value, end=" ")
    
    # Recursive case
    elif level > 1:
        print_current_level(root.left, level-1)
        print_current_level(root.right, level-1)

    


r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# inorder(r)
# print("\n")
# delete(r, 50)
# inorder(r)
print(print_level_order(r))
