# BST
# Node
class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

# Insertion      
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

def insert(root, key):
    new_node = Node(key)

    if root is None:
        root = new_node
        return root
    
    curr = root
    parent = root

    while curr:
        parent = curr
        if curr.value > key:
            curr = curr.left
        else:
            curr = curr.right 

    if parent.value < key:
        parent.right = new_node
    else:
        parent.left = new_node

    return root  
    
        

# In-order traversal: Left-Root-Right
# def inorder(root):
#     if root is None:
#         return  
   
#     inorder(root.left)
#     print(root.value, end="  ->  ")
#     inorder(root.right)

def inorder(root):
    if root is None:
        return
    
    curr = root
    while curr:
        print(curr.left.value, end="  ->  ")
        print(curr.value, end="  ->  ")
        print(curr.right.value, end="  ->  ")
        if curr.left:
            curr = curr.left
        else:
            curr = curr.right
    

        

# Pre-order traversal: Root-Left-Right
def preorder(root):
    if root is None:
        return
    
    print(root.value, end="  ->  ")
    preorder(root.left)
    preorder(root.right)

# Post-order traversal: Left-Right-Root
def postorder(root):
    if root is None:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.value, end="  ->  ")


r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# Print inorder traversal of the BST
print("In-order")
inorder(r)
# print("\n")
# print("Pre-order")
# preorder(r)
# print("\n")
# print("Post-order")
# postorder(r)

    