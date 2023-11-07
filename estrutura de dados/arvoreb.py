class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def remove(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = remove(root.left, key)
    elif key > root.val:
        root.right = remove(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.val = minValueNode(root.right)
        root.right = remove(root.right, root.val)
    return root

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.val

def preOrder(root):
    if root:
        print(root.val)
        preOrder(root.left)
        preOrder(root.right)

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.val)

# Criar a Árvore Binária com a sequência {60, 50, 70, 40, 65, 55, 75}
root = None
sequence = [60, 50, 70, 40, 65, 55, 75]
for item in sequence:
    root = insert(root, item)

print("Árvore Binária Original:")
print("Pré-Ordem: ")
preOrder(root)
print("\nEm-Ordem: ")
inOrder(root)
print("\nPós-Ordem: ")
postOrder(root)

# Remover o nó 50
root = remove(root, 50)

print("\n\nÁrvore após remoção do nó 50:")
print("Pré-Ordem: ")
preOrder(root)
print("\nEm-Ordem: ")
inOrder(root)
print("\nPós-Ordem: ")
postOrder(root)

# Remover o nó 60
root = remove(root, 60)

print("Árvore após remoção do nó 60:")
print("Pré-Ordem: ")
preOrder(root)
print("Em-Ordem: ")
inOrder(root)
print("Pós-Ordem: ")
postOrder(root)
