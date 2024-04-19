

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def add_left(self, node):
        self.left = node
    def add_right(self, node):
        self.right = node

def init_node(left, sourceString):

    if left == None and len(sourceString) >= 3:
        parent = Node(sourceString[1])
        parent.left = Node(sourceString[0])
        parent.right = Node(sourceString[2])
        if len(sourceString) == 3:
            return parent
        else:
            return init_node(parent, sourceString[3:])

    if left != None and len(sourceString) >= 2:
        parent = Node(sourceString[0])
        parent.left = left
        parent.right = Node(sourceString[1])
        if len(sourceString) == 2:
            return parent
        else:
            return init_node(parent, sourceString[2:])



def inorder(tree: Node):
    if tree:
        inorder(tree.left)
        print(tree.data + " ")
        inorder(tree.right)
def iterinorder(tree: Node):
        node = tree
        L = []
        while True:
            while node != None:
                L.append(node)
                node = node.left
            if len(L) == 0:
                break
            popped = L.pop()
            if popped == None:
                break
            print(popped.data)
            node = popped.right



def preorder(tree: Node):
    if tree:
        print(tree.data + " ")
        preorder(tree.left)
        preorder(tree.right)

def postorder(tree: Node):
    if tree:
        postorder(tree.left)
        postorder(tree.right)
        print(tree.data + " ")



node = init_node(None,"A/B*C*D+E")
print("inorder")
inorder(node)
print("\n")

print("preorder")
preorder(node)
print("\n")

print("postorder")
postorder(node)
print("\n")

print("iter inorder")
iterinorder(node)
print("\n")